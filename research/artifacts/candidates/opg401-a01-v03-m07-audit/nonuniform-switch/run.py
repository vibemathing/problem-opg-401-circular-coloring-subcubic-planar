"""Bounded, stdlib-only frontend replay; never invokes a repository verifier."""
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
LIMITS={'wall_seconds':20,'cpu_seconds':10,'address_space_bytes':268435456,
        'file_bytes':1048576,'stdout_stderr_bytes':65536,'threads':1,'retries':0}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bound():
    resource.setrlimit(resource.RLIMIT_CPU,(10,10))
    resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
    resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
def main():
    env={'PATH':os.defpath,'LANG':'C.UTF-8','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'}
    begin=time.monotonic();timed_out=False
    with (ROOT/'stdout.txt').open('wb') as out,(ROOT/'stderr.txt').open('wb') as err:
        p=subprocess.Popen([sys.executable,'-I','-S','audit.py'],cwd=ROOT,env=env,
                           stdout=out,stderr=err,start_new_session=True,preexec_fn=bound)
        try:p.wait(timeout=LIMITS['wall_seconds'])
        except subprocess.TimeoutExpired:
            timed_out=True;os.killpg(p.pid,signal.SIGKILL);p.wait(timeout=3)
    stdout=(ROOT/'stdout.txt').read_bytes();stderr=(ROOT/'stderr.txt').read_bytes()
    output_limit=max(len(stdout),len(stderr)) > LIMITS['stdout_stderr_bytes']
    names=['input.json','audit.py','run.py','certificate.json']
    record={'verdict':'candidate_only','trust_domain':'candidate_generator',
            'execution':'executed_frontend_bounded','command':['python3','-I','-S','audit.py'],
            'python':platform.python_version(),'implementation':platform.python_implementation(),
            'python_binary_sha256':digest(Path(sys.executable)),'limits':LIMITS,
            'wall_seconds_observed':round(time.monotonic()-begin,6),'exit_status':p.returncode,
            'timed_out':timed_out,'output_limit_exceeded':output_limit,
            'stdout':stdout[:65536].decode('utf-8','replace'),
            'stdout_sha256':hashlib.sha256(stdout).hexdigest(),'stderr_sha256':hashlib.sha256(stderr).hexdigest(),
            'stderr_bytes':len(stderr),
            'files':[{'name':n,'bytes':(ROOT/n).stat().st_size,'sha256':digest(ROOT/n)} for n in names if (ROOT/n).is_file()],
            'scope':'finite controls only; no arbitrary exterior enumeration',
            'network_calls_in_child':0,'trusted_verifier_receipt':False,'lean_smt_invoked':False}
    (ROOT/'execution.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['python','exit_status','timed_out','wall_seconds_observed','stdout']}))
    if p.returncode != 0 or timed_out or output_limit:raise SystemExit(1)
if __name__ == '__main__':main()
