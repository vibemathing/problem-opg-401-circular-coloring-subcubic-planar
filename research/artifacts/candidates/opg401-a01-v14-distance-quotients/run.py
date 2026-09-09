#!/usr/bin/env python3
import os,resource,subprocess,sys,time
H=os.path.dirname(os.path.abspath(__file__))
def lim():
 resource.setrlimit(resource.RLIMIT_CPU,(10,10));resource.setrlimit(resource.RLIMIT_AS,(128*1024*1024,128*1024*1024));resource.setrlimit(resource.RLIMIT_FSIZE,(1024*1024,1024*1024))
t=time.monotonic();p=subprocess.run([sys.executable,'-I','-S',os.path.join(H,'check.py')],cwd=H,capture_output=True,text=True,timeout=20,preexec_fn=lim);e=time.monotonic()-t
if len(p.stdout.encode())+len(p.stderr.encode())>65536:raise SystemExit('output budget')
sys.stdout.write(p.stdout);sys.stderr.write(p.stderr);print(f'runner_elapsed_seconds={e:.6f}',file=sys.stderr);raise SystemExit(p.returncode)
