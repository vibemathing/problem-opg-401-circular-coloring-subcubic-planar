#!/usr/bin/env python3
import os,resource,subprocess,sys,time
H=os.path.dirname(os.path.abspath(__file__))
def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(20,20))
    resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,256*1024*1024))
    resource.setrlimit(resource.RLIMIT_FSIZE,(2*1024*1024,2*1024*1024))
start=time.monotonic()
p=subprocess.run([sys.executable,"-I","-S",os.path.join(H,"check.py")],
                 cwd=H,capture_output=True,text=True,timeout=30,preexec_fn=limits)
elapsed=time.monotonic()-start
if len(p.stdout.encode())+len(p.stderr.encode())>65536:
    raise SystemExit("output budget exceeded")
sys.stdout.write(p.stdout);sys.stderr.write(p.stderr)
print(f"runner_elapsed_seconds={elapsed:.6f}",file=sys.stderr)
raise SystemExit(p.returncode)
