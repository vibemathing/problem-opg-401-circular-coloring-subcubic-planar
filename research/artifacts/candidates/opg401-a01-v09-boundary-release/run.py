"""Reproduce finite candidate controls; not a trusted verifier adapter."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib,json,platform,resource,subprocess,sys,time

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def limits():
 resource.setrlimit(resource.RLIMIT_CPU,(20,20))
 resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,256*1024*1024))
 resource.setrlimit(resource.RLIMIT_FSIZE,(2*1024*1024,2*1024*1024))
 resource.setrlimit(resource.RLIMIT_CORE,(0,0))

def main():
 root=Path(__file__).resolve().parent
 if any((root/p).exists() for p in ('certificate.json','execution.json')):
  raise SystemExit('Use a fresh directory; refusing to overwrite recorded outputs.')
 inputs={p:digest(root/p) for p in ('proof.md','check.py','input.json','run.py')}
 start=datetime.now(timezone.utc).isoformat();tick=time.monotonic()
 try:
  run=subprocess.run([sys.executable,'-I','-S','check.py'],cwd=root,capture_output=True,
                     timeout=30,preexec_fn=limits,check=False)
  timed_out=False;code=run.returncode;stdout=run.stdout;stderr=run.stderr
 except subprocess.TimeoutExpired as e:
  timed_out=True;code=None;stdout=e.stdout or b'';stderr=e.stderr or b''
 elapsed=time.monotonic()-tick
 output_ok=len(stdout)+len(stderr)<=65536
 record={'schema':'candidate-execution-v1','verdict':'candidate_only',
  'trust_domain':'candidate_generator_frontend','registered_verifier_invoked':False,
  'started_at':start,'finished_at':datetime.now(timezone.utc).isoformat(),
  'command':['python3','-I','-S','check.py'],'python':platform.python_version(),
  'implementation':platform.python_implementation(),'interpreter_sha256':digest(Path(sys.executable)),
  'input_sha256':inputs,'exit_code':code,'timeout':timed_out,'wall_seconds':round(elapsed,6),
  'limits':{'wall_seconds':30,'cpu_seconds':20,'address_space_bytes':268435456,
   'file_bytes':2097152,'combined_output_bytes':65536,'output_limit_enforcement':'checked_after_bounded_return',
   'threads':1,'retries':0},
  'stdout_bytes':len(stdout),'stderr_bytes':len(stderr),
  'stdout_sha256':hashlib.sha256(stdout).hexdigest(),'stderr_sha256':hashlib.sha256(stderr).hexdigest(),
  'output_budget_pass':output_ok,'output_sha256':{}}
 if (root/'certificate.json').exists():record['output_sha256']['certificate.json']=digest(root/'certificate.json')
 if code==0 and output_ok and not timed_out:record['observed_counts']=json.loads(stdout.decode('utf-8'))
 (root/'execution.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
 if timed_out or code!=0 or not output_ok:raise SystemExit('Finite control failed; inspect the execution record, not a mathematical negative.')
 print(json.dumps(record['observed_counts'],sort_keys=True))
if __name__=='__main__':main()
