"""Execute the fixed suite, preserving raw pytest output and actual outcomes."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    output = ROOT / args.output
    if output.exists():
        prior = json.loads(output.read_text(encoding='utf-8'))
        if prior.get('execution_status') != 'not_run':
            parser.error('Output already exists; choose a new name to preserve evidence.')
    output.parent.mkdir(parents=True, exist_ok=True)
    xml_path = output.with_suffix('.xml')
    start = datetime.now(timezone.utc).isoformat()
    tick = time.perf_counter()
    proc = subprocess.run([sys.executable, '-m', 'pytest', 'tests/test_fixed.py', '-v',
                           '--junitxml=' + str(xml_path)], cwd=ROOT, capture_output=True, text=True)
    elapsed = time.perf_counter() - tick
    raw = proc.stdout + proc.stderr
    output.with_suffix('.log').write_text(raw, encoding='utf-8')
    print(raw)
    results = []
    if xml_path.exists():
        for case in ET.parse(xml_path).iter('testcase'):
            state = 'passed'
            for tag, status in [('failure', 'failed'), ('error', 'errors'), ('skipped', 'skipped')]:
                if case.find(tag) is not None:
                    state = status
                    break
            parts = case.attrib['name'].split('_')
            results.append({'id': parts[1] if len(parts) > 1 else 'collection_error',
                            'function': case.attrib['name'], 'status': state})
    counts = {status: sum(r['status'] == status for r in results)
              for status in ('passed', 'failed', 'errors', 'skipped')}
    expected_ids = [f'T{i:02}' for i in range(1, 11)]
    valid = sorted(r['id'] for r in results) == expected_ids
    git_result = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True)
    data = {'execution_status': 'executed', 'total': len(results), **counts, 'results': results,
            'started_at': start, 'ended_at': datetime.now(timezone.utc).isoformat(),
            'elapsed_seconds': elapsed, 'python': sys.version, 'pytest_exit_code': proc.returncode,
            'collection_valid': valid,
            'hashes': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                       for name in ('tests/test_fixed.py', 'tests/conftest.py', 'evidence/fixed-contract.json')},
            'git_sha': git_result.stdout.strip() if git_result.returncode == 0 else None,
            'git_measurement_status': 'available' if git_result.returncode == 0 else 'unavailable'}
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return proc.returncode if proc.returncode else (0 if valid else 2)


if __name__ == '__main__':
    sys.exit(main())
