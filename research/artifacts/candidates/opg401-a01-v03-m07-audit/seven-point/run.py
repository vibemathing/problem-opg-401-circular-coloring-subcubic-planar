"""Run one bounded replay phase per call, then assemble the actual observations."""
import hashlib,json,os,platform,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
LIMIT={'wall_seconds':40,'cpu_seconds':35,'memory_bytes':536870912,'output_file_bytes':1048576,'threads':1,'retries':0}
PHASES={'generate':['finite.py','--generate'],'check':['finite.py'],'recolor':['recolor.py']}
SOURCES=['finite.py','recolor.py','run.py','proof.md']
OUTPUTS=['cover.json','synthesis.json','check-result.json','recolor-certificate.json']
def limits():
 resource.setrlimit(resource.RLIMIT_CPU,(35,35));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912));resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def meta(names):return [{'name':n,'bytes':(ROOT/n).stat().st_size,'sha256':digest(ROOT/n)} for n in names]
def main():
 phase=sys.argv[1] if len(sys.argv)==2 else 'help'
 if phase=='summarize':
  records=[json.loads((ROOT/(k+'-execution.json')).read_text()) for k in PHASES]
  assert all(r['exit_status']==0 and r['sources']==meta(SOURCES) for r in records)
  result={'verdict':'candidate_only','trust_domain':'candidate_generator','python_version':platform.python_version(),'implementation':platform.python_implementation(),'python_binary_sha256':digest(Path(sys.executable)),'limits_per_child':LIMIT,'runs':records,'files':meta(SOURCES+OUTPUTS),'trusted_verifier_receipt':False,'earlier_probes':'An unoptimized synthesis reached its wall cap; an insufficient reflection mutation witness failed; combined multi-phase caller windows were interrupted before a receipt. These exploratory failures were repaired and are not mathematical counterexamples. Final phases are executed separately.'}
  (ROOT/'execution.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'phases':list(PHASES),'exit_statuses':[r['exit_status'] for r in records],'seconds':[r['wall_seconds'] for r in records]}));return
 if phase not in PHASES:raise SystemExit('usage: run.py generate|check|recolor|summarize')
 start=time.monotonic();source=meta(SOURCES)
 p=subprocess.run([sys.executable,'-I','-S']+PHASES[phase],cwd=ROOT,env={'PATH':os.defpath,'LANG':'C.UTF-8','OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1'},capture_output=True,timeout=40,preexec_fn=limits)
 assert len(p.stdout)<65536 and len(p.stderr)<65536
 record={'command':['python3','-I','-S']+PHASES[phase],'exit_status':p.returncode,'wall_seconds':round(time.monotonic()-start,6),'stdout':p.stdout.decode(),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest(),'sources':source}
 (ROOT/(phase+'-execution.json')).write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
 if p.returncode:raise SystemExit(1)
if __name__=='__main__':main()
