"""Bounded reproducible candidate replay; never a verifier/admission receipt."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,platform,resource,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'replay'
if OUT.exists():raise SystemExit('replay already exists; use a fresh copy')
OUT.mkdir()
def sha(b):return hashlib.sha256(b).hexdigest()
source={}
for name in ('check.py','input.json','proof.md','run.py'):
    b=(ROOT/name).read_bytes();source[name]=sha(b)
    if name in ('check.py','input.json'):(OUT/name).write_bytes(b)
limits={'wall_seconds':30,'cpu_seconds':20,'address_space_bytes':268435456,
        'file_bytes':2097152,'captured_output_bytes':65536,'threads':1,'retries':0}
def cap():
    resource.setrlimit(resource.RLIMIT_CPU,(20,20))
    resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))
    resource.setrlimit(resource.RLIMIT_FSIZE,(2097152,2097152))
t=time.monotonic();timed_out=False
try:
    r=subprocess.run([sys.executable,'-I','-S','check.py'],cwd=OUT,
        capture_output=True,timeout=30,preexec_fn=cap,check=False)
    code=r.returncode;stdout=r.stdout;stderr=r.stderr
except subprocess.TimeoutExpired as e:
    code=None;timed_out=True;stdout=e.stdout or b'';stderr=e.stderr or b''
if len(stdout)+len(stderr)>65536:raise SystemExit('captured output limit exceeded')
outputs={}
for name in ('certificate.json',):
    path=OUT/name
    if path.exists():outputs[name]=sha(path.read_bytes())
record={'kind':'candidate_frontend_execution','verdict':'candidate_only',
        'recorded_at_utc':datetime.now(timezone.utc).isoformat(),
        'python_version':platform.python_version(),'implementation':platform.python_implementation(),
        'interpreter_sha256':sha(Path(sys.executable).read_bytes()),
        'sources_sha256':source,'outputs_sha256':outputs,
        'limits':limits,'exit_code':code,'timeout':timed_out,'elapsed_seconds':round(time.monotonic()-t,6),
        'stdout_utf8':stdout.decode('utf-8'),'stdout_sha256':sha(stdout),'stderr_utf8':stderr.decode('utf-8'),
        'stderr_sha256':sha(stderr),'command':['python3','-I','-S','check.py'],
        'scope':'Same candidate-generator trust domain; no registered verifier or admission.'}
(OUT/'execution.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps({'exit_code':code,'timeout':timed_out,'outputs_sha256':outputs,'stdout':record['stdout_utf8']}))
if code!=0 or timed_out:raise SystemExit(1)
