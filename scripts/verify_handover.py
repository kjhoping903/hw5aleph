import ast
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
HEADINGS = ['현재 상태와 목표','고정 검사 10개','환경 재현 방법','수정한 주요 파일',
            '남은 문제 및 제한사항','Session B 다음 행동','검증 및 측정 지표']


def verify():
    issues = []
    path = ROOT/'handover.md'
    if not path.exists():
        return ['handover.md missing']
    text = path.read_text(encoding='utf-8')
    for i,heading in enumerate(HEADINGS,1):
        if f'## {i}. {heading}' not in text:
            issues.append(f'missing heading {i}')
    for name in ('README.md','app.py','Dockerfile','compose.yaml','docs/test-plan.md',
                 'scripts/run_tests.py','evidence/session-a-results.json'):
        if not (ROOT/name).exists():
            issues.append('missing file '+name)
    try:
        expected = json.loads((ROOT/'evidence/frozen-hashes.json').read_text(encoding='utf-8'))
        for name,digest in expected.items():
            if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != digest:
                issues.append('hash mismatch '+name)
        contract = json.loads((ROOT/'evidence/fixed-contract.json').read_text(encoding='utf-8'))
        if [c['id'] for c in contract['checks']] != [f'T{i:02}' for i in range(1,11)]:
            issues.append('contract IDs mismatch')
        functions = [n.name for n in ast.parse((ROOT/'tests/test_fixed.py').read_text(encoding='utf-8')).body
                     if isinstance(n, ast.FunctionDef)]
        if functions != [c['function'] for c in contract['checks']]:
            issues.append('test functions mismatch')
    except (OSError,ValueError,KeyError) as error:
        issues.append(str(error))
    if 'python scripts/run_tests.py --output evidence/session-b-start-results.json' not in text:
        issues.append('Next Action test command missing')
    return issues


if __name__ == '__main__':
    issues = verify()
    print(json.dumps({'status':'FAIL' if issues else 'PASS','issues':issues},ensure_ascii=False,indent=2))
    sys.exit(1 if issues else 0)
