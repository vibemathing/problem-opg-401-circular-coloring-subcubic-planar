"""One bounded frontend replay, with no trusted-verifier or admission claim."""
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
LIMITS={'wall_seconds':40,'cpu_seconds':35,'memory_bytes':536870912,'file_bytes':1048576,
        'output_bytes_after_return':65536,'threads':1,'retries':0}

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(35,35))
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
    resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))

def main():
    replay=ROOT/'replay'
    replay.mkdir(exist_ok=False)
    env={'PATH':os.defpath,'LANG':'C.UTF-8','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'}
    start=time.monotonic(); timed_out=False
    with (replay/'stdout.txt').open('wb') as stdout,(replay/'stderr.txt').open('wb') as stderr:
        proc=subprocess.Popen([sys.executable,'-I','-S','check.py','input.json','replay/certificate.json'],
                              cwd=ROOT,env=env,preexec_fn=limits,start_new_session=True,stdout=stdout,stderr=stderr)
        try:proc.wait(timeout=40)
        except subprocess.TimeoutExpired:
            timed_out=True;os.killpg(proc.pid,signal.SIGKILL);proc.wait(timeout=3)
    stdout=(replay/'stdout.txt').read_bytes();stderr=(replay/'stderr.txt').read_bytes()
    record={'verdict':'candidate_only','trust_domain':'candidate_generator',
            'command':['python3','-I','-S','check.py','input.json','replay/certificate.json'],
            'python_version':platform.python_version(),'python_binary_sha256':digest(Path(sys.executable)),
            'limits':LIMITS,'exit_status':proc.returncode,'timed_out':timed_out,
            'elapsed_seconds':round(time.monotonic()-start,6),
            'stdout':stdout.decode('utf-8'),'stdout_sha256':hashlib.sha256(stdout).hexdigest(),
            'stderr_bytes':len(stderr),'stderr_sha256':hashlib.sha256(stderr).hexdigest(),
            'files':[{'path':p,'bytes':(ROOT/p).stat().st_size,'sha256':digest(ROOT/p)}
                     for p in ['check.py','run.py','input.json','replay/certificate.json'] if (ROOT/p).exists()],
            'network_calls_in_child':'none in the executed source',
            'trusted_verifier_invoked':False,'lean_smt_invoked':False}
    (replay/'execution.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['exit_status','timed_out','elapsed_seconds','stdout','stderr_bytes']}))
    if timed_out or proc.returncode or len(stdout)+len(stderr)>65536: raise SystemExit(1)

if __name__=='__main__':main()
