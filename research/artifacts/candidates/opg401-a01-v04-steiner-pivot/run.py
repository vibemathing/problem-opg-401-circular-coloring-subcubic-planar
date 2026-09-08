"""Replay in a fresh directory; observations are candidate-generator data."""
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import shutil
import signal
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
LIMITS={'wall_seconds':20,'cpu_seconds':15,'memory_bytes':268435456,'file_bytes':1048576,
        'captured_output_bytes_checked_after_return':65536,'threads':1,'retries':0}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bound():
    resource.setrlimit(resource.RLIMIT_CPU,(15,15))
    resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
    resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
def main():
    out=HERE/'replay'
    out.mkdir(exist_ok=False)
    for name in ('check.py','input.json'):shutil.copyfile(HERE/name,out/name)
    env={'PATH':os.defpath,'LANG':'C.UTF-8','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'}
    start=time.monotonic()
    with (out/'stdout.txt').open('wb') as stdout,(out/'stderr.txt').open('wb') as stderr:
        child=subprocess.Popen([sys.executable,'-I','-S','check.py'],cwd=out,env=env,
                               preexec_fn=bound,stdout=stdout,stderr=stderr,start_new_session=True)
        timeout=False
        try:child.wait(timeout=20)
        except subprocess.TimeoutExpired:
            timeout=True;os.killpg(child.pid,signal.SIGKILL);child.wait(timeout=3)
    stdout=(out/'stdout.txt').read_bytes();stderr=(out/'stderr.txt').read_bytes()
    if len(stdout)+len(stderr)>65536:raise RuntimeError('captured-output cap exceeded')
    record={'verdict':'candidate_only','trust_domain':'candidate_generator','python_version':platform.python_version(),
            'implementation':platform.python_implementation(),'python_binary_sha256':digest(Path(sys.executable)),
            'command':['python3','-I','-S','check.py'],'limits':LIMITS,'exit_status':child.returncode,
            'timed_out':timeout,'wall_seconds':round(time.monotonic()-start,6),
            'source_inputs':[{'name':n,'sha256':digest(HERE/n),'bytes':(HERE/n).stat().st_size} for n in ('check.py','input.json','run.py')],
            'stdout':stdout.decode(),'stdout_sha256':hashlib.sha256(stdout).hexdigest(),
            'stderr_bytes':len(stderr),'stderr_sha256':hashlib.sha256(stderr).hexdigest(),
            'network_used':False,'registered_verifier_invoked':False}
    if (out/'certificate.json').exists():
        record['certificate_sha256']=digest(out/'certificate.json')
        record['certificate_bytes']=(out/'certificate.json').stat().st_size
    (out/'execution.json').write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps(record,sort_keys=True))
    if child.returncode or timeout:raise SystemExit(1)
if __name__=='__main__':main()
