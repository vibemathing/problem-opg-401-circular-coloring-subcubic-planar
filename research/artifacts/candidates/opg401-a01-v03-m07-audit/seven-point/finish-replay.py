"""Bounded final byte-replay observations; candidate generator only."""
import hashlib,json,os,platform,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SOURCES=['finite.py','recolor.py','assemble-cover.py','finish-replay.py']
PHASES={'check':['finite.py'],'recolor':['recolor.py']}
LIMITS={'wall_seconds':40,'cpu_seconds':35,'memory_bytes':536870912,'file_bytes':1048576,'threads':1,'retries':0}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def cap():
 resource.setrlimit(resource.RLIMIT_CPU,(35,35));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912));resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
phase=sys.argv[1]
if phase not in PHASES:raise SystemExit('usage: finish-replay.py check|recolor')
begin=time.monotonic()
p=subprocess.run([sys.executable,'-I','-S']+PHASES[phase],cwd=ROOT,env={'PATH':os.defpath,'LANG':'C.UTF-8','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'},capture_output=True,timeout=40,preexec_fn=cap)
if len(p.stdout)>65536 or len(p.stderr)>65536:raise RuntimeError('output cap exceeded')
record={'verdict':'candidate_only','trust_domain':'candidate_generator','phase':phase,'command':['python3','-I','-S']+PHASES[phase],'python_version':platform.python_version(),'implementation':platform.python_implementation(),'python_binary_sha256':sha(Path(sys.executable)),'limits':LIMITS,'exit_status':p.returncode,'wall_seconds':round(time.monotonic()-begin,6),'stdout':p.stdout.decode(),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest(),'sources':[{'name':s,'sha256':sha(ROOT/s)} for s in SOURCES],'input_cover_sha256':sha(ROOT/'cover.json'),'output_sha256':sha(ROOT/('check-result.json' if phase=='check' else 'recolor-certificate.json')),'trusted_verifier_receipt':False}
(ROOT/(phase+'-final-replay.json')).write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
if p.returncode:raise SystemExit(1)
