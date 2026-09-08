"""Bounded local replay. Linux resource limits; candidate-generation role only."""
from __future__ import annotations
import datetime,hashlib,json,os,pathlib,platform,resource,shutil,signal,subprocess,sys,time
D=pathlib.Path(__file__).resolve().parent

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def bounded(argv,cpu,wall,memory):
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(cpu,cpu))
        resource.setrlimit(resource.RLIMIT_AS,(memory,memory))
        resource.setrlimit(resource.RLIMIT_FSIZE,(2097152,2097152))
        resource.setrlimit(resource.RLIMIT_NOFILE,(64,64))
    start=time.monotonic()
    env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
    # Each bounded root owns its group; kill descendants too on timeout.
    proc=subprocess.Popen(argv,cwd=D,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                          preexec_fn=limits,env=env,start_new_session=True)
    try:
        stdout,stderr=proc.communicate(timeout=wall)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid,signal.SIGKILL)
        proc.communicate()
        raise RuntimeError('bounded process group timed out') from None
    res=subprocess.CompletedProcess(argv,proc.returncode,stdout,stderr)
    if len(res.stdout)>65536 or len(res.stderr)>65536:raise RuntimeError('output cap')
    rec=dict(command=argv,exit_status=res.returncode,wall_seconds=round(time.monotonic()-start,6),limits=dict(cpu_seconds=cpu,wall_seconds=wall,address_space_bytes=memory,file_bytes=2097152,stdout_stderr_bytes_each=65536,threads=1,retries=0),stdout_sha256=hashlib.sha256(res.stdout).hexdigest(),stderr_sha256=hashlib.sha256(res.stderr).hexdigest(),stdout=res.stdout.decode().strip())
    if res.returncode:raise RuntimeError(json.dumps(rec))
    return rec

def main():
    compiler=shutil.which('g++')
    if compiler is None:raise RuntimeError('g++ required; no install attempted')
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    runs=[bounded(['g++','--version'],2,5,134217728)]
    runs.append(bounded(['g++','-std=c++20','-O2','-Wall','-Wextra','-Werror','exact_color.cpp','-o','exact_color'],12,15,536870912))
    runs.append(bounded(['python3','-I','-S','audit.py'],30,40,268435456))
    names=['fixtures.json','exact_color.cpp','audit.py','run.py','tables.json','mutations.json','gadget-search.json','processes.json']
    assert sum((D/n).stat().st_size for n in names)<2097152
    report=dict(verdict='candidate_only',status='executed_frontend_bounded',started_at=started,python_version=platform.python_version(),python_binary_sha256=digest(pathlib.Path(sys.executable)),compiler_binary_sha256=digest(pathlib.Path(compiler)),compiled_candidate_binary_sha256=digest(D/'exact_color'),route='CPU exact integers; no CAS, SAT, GPU or Lean',trust_role='candidate_generator',repository_verifier_adapter='not_invoked',producer_limits=dict(max_retained_text_files=9,max_retained_text_bytes=2097152),runs=runs,files=[dict(path=n,bytes=(D/n).stat().st_size,sha256=digest(D/n)) for n in names])
    (D/'execution.json').write_text(json.dumps(report,indent=2)+'\n')
    print(runs[-1]['stdout'])
if __name__=='__main__':main()
