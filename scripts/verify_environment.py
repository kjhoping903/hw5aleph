import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ['app.py','requirements.txt','requirements-dev.txt','Dockerfile','compose.yaml',
            '.env.example','README.md','AGENTS.md','handover.md','tests/test_fixed.py',
            'evidence/fixed-contract.json','evidence/frozen-hashes.json']


def inspect():
    docker = shutil.which('docker')
    compose = {'status':'not_run','reason':'docker command not found'}
    if docker:
        result = subprocess.run([docker,'compose','version'],capture_output=True,text=True)
        compose = {'status':'pass' if result.returncode == 0 else 'fail',
                   'exit_code':result.returncode,'output':result.stdout + result.stderr}
    return {'python':platform.python_version(), 'python_3_12':sys.version_info[:2] == (3,12),
            'docker_command_exists':bool(docker),'compose':compose,
            'required_files':{name:(ROOT/name).is_file() for name in REQUIRED},
            'environment_variable_names':['APP_PLACE'], 'secret_values_printed':False}


if __name__ == '__main__':
    result = inspect()
    print(json.dumps(result,ensure_ascii=False,indent=2))
    sys.exit(0 if result['python_3_12'] and all(result['required_files'].values()) and result['compose']['status'] == 'pass' else 1)
