"""Bounded candidate-generator replay; no trusted verifier is invoked."""
import hashlib,json,os,platform,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
LIMITS={'wall_seconds':30,'cpu_seconds':20,'memory_bytes':268435456,'file_bytes':2097152,'output_bytes_postcheck':65536,'threads':1,'retries':0}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bounds():
    resource.setrlimit(resource.RLIMIT_CPU,(20,20))
    resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
    resource.setrlimit(resource.RLIMIT_FSIZE,(2097152,2097152))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
def main():
    for name in ['fork-certificate.json','case-p1.json','case-p14.json','execution.json']:
        if (ROOT/name).exists():raise RuntimeError('Replay in a fresh copy; preserve previous observations')
    start=time.monotonic();timed=False
    try:
        p=subprocess.run([sys.executable,'-I','-S','check.py'],cwd=ROOT,env={'PATH':os.defpath,'LANG':'C.UTF-8','OMP_NUM_THREADS':'1'},
          preexec_fn=bounds,capture_output=True,timeout=30)
        code,out,err=p.returncode,p.stdout,p.stderr
    except subprocess.TimeoutExpired as exc:
        timed=True;code=None;out=exc.stdout or b'';err=exc.stderr or b''
    oversized=len(out)+len(err)>65536
    files=['check.py','input.json','run.py','fork-certificate.json','case-p1.json','case-p14.json']
    record={'verdict':'candidate_only','trust_domain':'candidate_generator','command':['python3','-I','-S','check.py'],
      'python_version':platform.python_version(),'implementation':platform.python_implementation(),
      'binary_sha256':sha(Path(sys.executable)),'limits':LIMITS,'exit_status':code,'timed_out':timed,'oversized_output':oversized,
      'elapsed_seconds':round(time.monotonic()-start,6),'stdout_sha256':hashlib.sha256(out).hexdigest(),'stderr_sha256':hashlib.sha256(err).hexdigest(),
      'stdout':out.decode('utf-8') if not oversized else None,'stderr_bytes':len(err),
      'files':[{'path':name,'bytes':(ROOT/name).stat().st_size,'sha256':sha(ROOT/name)} for name in files if (ROOT/name).exists()],
      'network_used':False,'trusted_verifier_run':None,'mathematical_scope':'Finite C1 control objects only; general claims have separate proofs.'}
    (ROOT/'execution.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({key:record[key] for key in ['exit_status','timed_out','elapsed_seconds','stdout','stderr_bytes']}))
    if code!=0 or timed or oversized:raise SystemExit(1)
if __name__=='__main__':main()
