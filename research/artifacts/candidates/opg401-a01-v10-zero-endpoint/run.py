"""Bounded candidate-generator replay; no trusted verification or admission."""
from pathlib import Path
import datetime,hashlib,json,os,resource,subprocess,sys,time
ROOT=Path(__file__).resolve().parent

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def bounds():
    resource.setrlimit(resource.RLIMIT_CPU,(20,20))
    resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,)*2)
    resource.setrlimit(resource.RLIMIT_FSIZE,(2*1024*1024,)*2)

if __name__=='__main__':
    for name in ('certificate.json','execution.json'):
        if (ROOT/name).exists():raise FileExistsError(name+' exists; use a fresh directory')
    sources={n:digest(ROOT/n) for n in ('check.py','input.json','run.py')}
    begin=datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.monotonic()
    env=os.environ.copy()
    env.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONHASHSEED='0')
    timed_out=False
    try:
        r=subprocess.run([sys.executable,'-I','-S','check.py'],cwd=ROOT,
                         capture_output=True,timeout=30,preexec_fn=bounds,env=env)
        code=r.returncode;stdout=r.stdout;stderr=r.stderr
    except subprocess.TimeoutExpired as e:
        timed_out=True;code=None;stdout=e.stdout or b'';stderr=e.stderr or b''
    size_ok=len(stdout)+len(stderr)<=65536
    record=dict(verdict='candidate_only',trusted_verifier=False,started_utc=begin,
      runtime=sys.version,interpreter_sha256=digest(Path(sys.executable)),
      command=['python3','-I','-S','check.py'],sources=sources,
      limits=dict(wall_seconds=30,cpu_seconds=20,address_space_bytes=268435456,
        file_bytes=2097152,combined_output_bytes=65536,output_check='after bounded capture',threads=1,retries=0),
      exit_code=code,timeout=timed_out,elapsed_seconds=time.monotonic()-start,output_budget_ok=size_ok,
      stdout_sha256=hashlib.sha256(stdout).hexdigest(),stderr_sha256=hashlib.sha256(stderr).hexdigest(),
      stdout=stdout.decode('utf-8') if size_ok else None,
      certificate_sha256=digest(ROOT/'certificate.json') if (ROOT/'certificate.json').exists() else None)
    (ROOT/'execution.json').write_text(json.dumps(record,indent=2)+'\n')
    if code!=0 or timed_out or not size_ok:
        if size_ok:print(stderr.decode('utf-8'),file=sys.stderr)
        raise SystemExit('candidate replay failed; no mathematical verdict')
    print(stdout.decode('utf-8'),end='')
