"""Bounded foreground runner for the finite palette audit only."""
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parent
LIMITS={'wall_seconds':10,'cpu_seconds':5,'address_space_bytes':134217728,
        'file_bytes':65536,'output_bytes':65536,'threads':1,'retries':0}

def bounds():
    for key,value in ((resource.RLIMIT_AS,134217728),(resource.RLIMIT_CPU,5),
                      (resource.RLIMIT_FSIZE,65536),(resource.RLIMIT_CORE,0)):
        resource.setrlimit(key,(value,value))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    start=time.monotonic()
    env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1',
         'MKL_NUM_THREADS':'1','PYTHONDONTWRITEBYTECODE':'1','PYTHONHASHSEED':'0'}
    p=subprocess.run([sys.executable,'-I','-S','palette_check.py'],cwd=ROOT,
                     env=env,preexec_fn=bounds,capture_output=True,timeout=10,check=False)
    if p.returncode or p.stderr or len(p.stdout)+len(p.stderr)>65536:
        raise RuntimeError('bounded palette audit failed; no success record')
    record={'verdict':'candidate_only','execution':'executed_frontend_bounded',
            'command':['python3','-I','-S','palette_check.py'],
            'python_version':platform.python_version(),'implementation':platform.python_implementation(),
            'python_binary_sha256':sha(Path(sys.executable)),'limits':LIMITS,
            'exit_status':p.returncode,'wall_seconds_observed':round(time.monotonic()-start,6),
            'stdout':p.stdout.decode().strip(),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),
            'stderr_sha256':hashlib.sha256(p.stderr).hexdigest(),
            'files':[{'name':n,'bytes':(ROOT/n).stat().st_size,'sha256':sha(ROOT/n)}
                     for n in ('input.json','palette_check.py','run.py','palette-audit.json')],
            'route':'CPU exact stdlib; isolated no-site runtime smoke passed in v01',
            'repository_compute_plan':'absent at frozen main; not invoked',
            'repository_verifier_adapter':'not_invoked','trusted_verifier_receipt':False,
            'scope':'finite palettes only; plane-patch theorem has a separate hand proof'}
    text=(json.dumps(record,indent=2)+'\n').encode()
    if len(text)>65536: raise RuntimeError('record cap')
    (ROOT/'execution.json').write_bytes(text)
    print(p.stdout.decode().strip())

if __name__=='__main__':
    main()
