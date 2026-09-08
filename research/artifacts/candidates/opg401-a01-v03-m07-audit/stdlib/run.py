"""Bounded foreground reproduction; not a registered mathematical verifier."""
from __future__ import annotations
import hashlib, json, os, platform, resource, subprocess, sys, time
from pathlib import Path

LIMITS = {'wall_seconds':40,'cpu_seconds':30,'address_space_bytes':536870912,
          'file_bytes':1048576,'stdout_bytes':65536,'threads':1,'retries':0,
          'producer_files':4,'producer_total_bytes':2097152}
OUTPUTS = ['extension-table.csv','residuals.json','three-port.json','audit.json']

def digest(p:Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def restrict() -> None:
    resource.setrlimit(resource.RLIMIT_AS,(LIMITS['address_space_bytes'],)*2)
    resource.setrlimit(resource.RLIMIT_CPU,(LIMITS['cpu_seconds'],)*2)
    resource.setrlimit(resource.RLIMIT_FSIZE,(LIMITS['file_bytes'],)*2)
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))

root=Path(__file__).resolve().parent
for name in OUTPUTS+['execution.json']:
    if (root/name).exists():
        raise SystemExit('Use a fresh copy of the source/input directory; existing outputs are never overwritten.')
env={'PATH':os.environ.get('PATH',''),'PYTHONHASHSEED':'0','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'}
t0=time.monotonic()
# Anonymous temporary files keep raw subprocess output out of the persistent package.
import tempfile
with tempfile.TemporaryFile() as out, tempfile.TemporaryFile() as err:
    proc=subprocess.Popen([sys.executable,'-I','-S','check.py'],cwd=root,env=env,stdout=out,stderr=err,preexec_fn=restrict)
    timeout=False
    try:
        proc.wait(timeout=LIMITS['wall_seconds'])
    except subprocess.TimeoutExpired:
        proc.kill();proc.wait();timeout=True
    out.seek(0);err.seek(0)
    stdout=out.read(LIMITS['stdout_bytes']+1);stderr=err.read(LIMITS['stdout_bytes']+1)
wall=time.monotonic()-t0
if len(stdout)>LIMITS['stdout_bytes'] or len(stderr)>LIMITS['stdout_bytes']:
    raise SystemExit('output cap exceeded; no success report')
files=[]
for name in ['check.py','run.py','input.json']+OUTPUTS:
    p=root/name
    if p.exists():files.append({'path':name,'bytes':p.stat().st_size,'sha256':digest(p)})
produced=[x for x in files if x['path'] in OUTPUTS]
if len(produced)>LIMITS['producer_files'] or sum(x['bytes'] for x in produced)>LIMITS['producer_total_bytes']:
    raise SystemExit('producer cap exceeded; no success report')
record={'verdict':'candidate_only','execution':'foreground_generator_crosscheck',
    'python_version':platform.python_version(),'implementation':platform.python_implementation(),
    'python_binary_sha256':digest(Path(sys.executable).resolve()),'command':['python3','-I','-S','check.py'],
    'limits':LIMITS,'elapsed_wall_seconds':round(wall,6),'exit_status':proc.returncode,'timed_out':timeout,
    'stdout_sha256':hashlib.sha256(stdout).hexdigest(),'stderr_sha256':hashlib.sha256(stderr).hexdigest(),
    'stdout':stdout.decode('utf-8'),'stderr':stderr.decode('utf-8') if not stderr else 'nonempty; inspect locally before transport',
    'files':files,'route':'CPU exact stdlib integers; no solver, GPU or Lean',
    'repository_compute_plan':'not invoked; unavailable in previously read source snapshot',
    'trusted_verifier_receipt':False}
(root/'execution.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'exit_status':proc.returncode,'seconds':round(wall,6),'outputs':len(produced),'status':'candidate_only'}))
if timeout or proc.returncode!=0 or len(produced)!=4:
    raise SystemExit(1)
