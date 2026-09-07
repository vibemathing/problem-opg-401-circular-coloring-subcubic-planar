"""Bounded POSIX frontend execution; not a repository verifier adapter.
Run from this file's directory: python3 run.py
"""
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
LIMITS = {"wall_seconds_per_process":10,"cpu_seconds_per_process":5,
          "address_space_bytes":134217728,"file_bytes":65536,
          "stdout_bytes":65536,"threads":1,"retries":0}

def limit_child() -> None:
    resource.setrlimit(resource.RLIMIT_AS,(LIMITS["address_space_bytes"],)*2)
    resource.setrlimit(resource.RLIMIT_CPU,(LIMITS["cpu_seconds_per_process"],)*2)
    resource.setrlimit(resource.RLIMIT_FSIZE,(LIMITS["file_bytes"],)*2)
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main() -> None:
    # Actual bounded stdlib smoke: no claimed repository tool installation.
    smoke = [sys.executable,"-I","-S","-c", "import json,hashlib; "
             "assert json.loads('{\"x\":7}')[\"x\"]==7; "
             "assert hashlib.sha256(b'abc').hexdigest()=="
             "'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'; "
             "print('stdlib-smoke-ok')"]
    commands = [smoke,[sys.executable,"-I","-S","enumerate.py","input.json","certificate.json"],
                [sys.executable,"-I","-S","check.py","input.json","certificate.json","audit.json"]]
    env = {**os.environ,"OMP_NUM_THREADS":"1","OPENBLAS_NUM_THREADS":"1",
           "MKL_NUM_THREADS":"1","PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0"}
    runs = []
    for command in commands:
        start = time.monotonic()
        run = subprocess.run(command,cwd=ROOT,env=env,preexec_fn=limit_child,
                             capture_output=True,timeout=10,check=False)
        if len(run.stdout)+len(run.stderr)>65536:
            raise RuntimeError("captured output bound exceeded")
        entry = {"command":["python3",*command[1:]],"exit_status":run.returncode,
                 "wall_seconds_observed":round(time.monotonic()-start,6),
                 "stdout_sha256":hashlib.sha256(run.stdout).hexdigest(),
                 "stderr_sha256":hashlib.sha256(run.stderr).hexdigest()}
        if run.returncode or run.stderr:
            raise RuntimeError("bounded subprocess failed; no success record written")
        entry["stdout"] = run.stdout.decode().strip()
        runs.append(entry)
    artifacts = ["input.json","enumerate.py","check.py","run.py","certificate.json","audit.json"]
    record = {"verdict":"candidate_only","execution":"executed_frontend_bounded",
              "python_version":platform.python_version(),"implementation":platform.python_implementation(),
              "python_binary_sha256":sha(Path(sys.executable)),
              "limits":LIMITS,"route":"CPU exact integer stdlib; no GPU, CAS, SAT or Lean",
              "repository_compute_plan":"not_present_at_frozen_main; no planner run claimed",
              "repository_verifier_adapter":"not_invoked","trust_domain":"candidate_generator",
              "runs":runs,"files":[{"name":n,"bytes":(ROOT/n).stat().st_size,
                                      "sha256":sha(ROOT/n)} for n in artifacts],
              "trusted_verifier_receipt":False}
    encoded=(json.dumps(record,indent=2)+"\n").encode()
    if len(encoded)>65536: raise RuntimeError("record cap")
    (ROOT/"execution.json").write_bytes(encoded)
    print(json.dumps({"execution":record["execution"],"python":record["python_version"],
                      "subprocesses":len(runs),"all_exit_zero":True}))

if __name__ == "__main__":
    main()
