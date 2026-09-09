#!/usr/bin/env python3
import os, resource, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
def limit():
    resource.setrlimit(resource.RLIMIT_CPU,(20,20))
    resource.setrlimit(resource.RLIMIT_AS,(256*1024*1024,256*1024*1024))
    resource.setrlimit(resource.RLIMIT_FSIZE,(2*1024*1024,2*1024*1024))
env={"PATH":os.environ.get("PATH",""),"PYTHONHASHSEED":"0","LC_ALL":"C","LANG":"C"}
p=subprocess.run([sys.executable,"-I","-S",str(HERE/"check.py")],
                 cwd=HERE,env=env,preexec_fn=limit,
                 stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                 timeout=30,check=False)
if len(p.stdout)+len(p.stderr)>65536:
    raise SystemExit("combined output exceeded 64 KiB")
sys.stdout.buffer.write(p.stdout);sys.stderr.buffer.write(p.stderr)
raise SystemExit(p.returncode)
