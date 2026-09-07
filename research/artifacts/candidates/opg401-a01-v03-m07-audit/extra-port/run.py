"""Bounded frontend replay; not a repository verifier or admission adapter."""
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import signal
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parent
LIMITS={'wall_seconds':20,'cpu_seconds':10,'memory_bytes':268435456,'file_bytes':1048576,'threads':1,'retries':0}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(10,10))
    resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
    resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))

def main():
    env={'PATH':os.defpath,'LANG':'C.UTF-8','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'}
    begin=time.monotonic()
    with (ROOT/'stdout.txt').open('wb') as out,(ROOT/'stderr.txt').open('wb') as err:
        proc=subprocess.Popen([sys.executable,'-I','-S','audit.py'],cwd=ROOT,env=env,stdout=out,stderr=err,
                              preexec_fn=limits,start_new_session=True)
        timed_out=False
        try:proc.wait(timeout=20)
        except subprocess.TimeoutExpired:
            timed_out=True;os.killpg(proc.pid,signal.SIGKILL);proc.wait(timeout=3)
    stdout=(ROOT/'stdout.txt').read_bytes();stderr=(ROOT/'stderr.txt').read_bytes()
    artifacts=['engine.py','audit.py','run.py','input.json','boundary-table.csv','audit.json','replacement-screen.json']
    record={'verdict':'candidate_only','trust_domain':'candidate_generator','execution':'executed_frontend_bounded',
            'command':['python3','-I','-S','audit.py'],'python_version':platform.python_version(),
            'implementation':platform.python_implementation(),'python_binary_sha256':sha(Path(sys.executable)),
            'limits':LIMITS,'wall_seconds_observed':round(time.monotonic()-begin,6),'exit_status':proc.returncode,
            'timed_out':timed_out,'stdout_sha256':hashlib.sha256(stdout).hexdigest(),
            'stderr_sha256':hashlib.sha256(stderr).hexdigest(),'stdout':stdout.decode('utf-8'),
            'stderr_bytes':len(stderr),'files':[{'name':n,'bytes':(ROOT/n).stat().st_size,'sha256':sha(ROOT/n)} for n in artifacts if (ROOT/n).exists()],
            'no_network_in_child':True,'repository_verifier_adapter':'not_invoked','trusted_verifier_receipt':False}
    (ROOT/'execution.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('exit_status','timed_out','wall_seconds_observed','stdout','stderr_bytes')}))
    if proc.returncode or timed_out:raise SystemExit(1)

if __name__=='__main__':main()
