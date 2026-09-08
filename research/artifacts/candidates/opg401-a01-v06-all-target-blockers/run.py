"""Bounded frontend candidate replay, not a verifier/admission adapter."""
from pathlib import Path
import hashlib,json,os,platform,resource,signal,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
LIMITS={'wall_seconds':30,'cpu_seconds':25,'memory_bytes':402653184,'file_bytes':2097152,
        'combined_output_bytes':65536,'threads':1,'retries':0}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(402653184,402653184))
    resource.setrlimit(resource.RLIMIT_FSIZE,(2097152,2097152));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
def main():
    env={'PATH':os.defpath,'LANG':'C.UTF-8','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'}
    start=time.monotonic();timed_out=False
    p=subprocess.Popen([sys.executable,'-I','-S','audit.py'],cwd=ROOT,env=env,
                        stdout=subprocess.PIPE,stderr=subprocess.PIPE,preexec_fn=limits,start_new_session=True)
    try:out,err=p.communicate(timeout=30)
    except subprocess.TimeoutExpired:
        timed_out=True;os.killpg(p.pid,signal.SIGKILL);out,err=p.communicate(timeout=2)
    output_ok=len(out)+len(err)<=65536
    record={'schema':'opg401-candidate-execution-v1','verdict':'candidate_only','trust_domain':'candidate_generator',
            'command':['python3','-I','-S','audit.py'],'python_version':platform.python_version(),
            'implementation':platform.python_implementation(),'python_binary_sha256':sha(Path(sys.executable)),
            'limits':LIMITS,'wall_seconds':round(time.monotonic()-start,6),'exit_status':p.returncode,
            'timed_out':timed_out,'output_within_budget':output_ok,
            'stdout_sha256':hashlib.sha256(out).hexdigest(),'stderr_sha256':hashlib.sha256(err).hexdigest(),
            'stdout':out.decode() if output_ok and not p.returncode else None,'stderr_bytes':len(err),
            'files':[{'path':n,'bytes':(ROOT/n).stat().st_size,'sha256':sha(ROOT/n)}
                     for n in ('input.json','audit.py','run.py','certificate.json') if (ROOT/n).is_file()],
            'prior_control_correction':'An exploratory assertion assumed every truncated failure path is invalid. A truncation may still end at a different forbidden vertex. The final mutation selects a truncation actually invalid under the scalar verifier. No mathematical claim was changed.',
            'trusted_verifier_run':None,'admission_run':None}
    (ROOT/'execution.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('exit_status','timed_out','wall_seconds','stdout','stderr_bytes')}))
    if p.returncode or timed_out or not output_ok:raise SystemExit(1)
if __name__=='__main__':main()
