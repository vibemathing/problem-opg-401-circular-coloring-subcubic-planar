import subprocess,sys,pathlib
root=pathlib.Path(__file__).resolve().parent
p=subprocess.run([sys.executable,"-I","-S",str(root/"check.py")],capture_output=True,text=True,timeout=20)
print(p.stdout.strip())
if p.returncode:
    print(p.stderr,file=sys.stderr)
    raise SystemExit(p.returncode)
