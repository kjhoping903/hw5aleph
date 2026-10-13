import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def collect(result_file):
    git = subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,capture_output=True,text=True)
    return {'collected_at':datetime.now(timezone.utc).isoformat(),
            'git_sha':git.stdout.strip() if git.returncode == 0 else None,
            'git_status':subprocess.run(['git','status','--porcelain'],cwd=ROOT,capture_output=True,text=True).stdout,
            'result_file':result_file, 'results':json.loads((ROOT/result_file).read_text(encoding='utf-8')),
            'file_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                           for p in ('app.py','tests/test_fixed.py','tests/conftest.py','evidence/fixed-contract.json')},
            'tokens':{'measurement_status':'unavailable','value':None},
            'internal_calls':{'measurement_status':'unavailable','value':None}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--result',required=True)
    parser.add_argument('--output',required=True)
    args = parser.parse_args()
    output = ROOT/args.output
    if output.exists():
        parser.error('Output exists; preserve previous evidence using another filename.')
    output.write_text(json.dumps(collect(args.result),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
