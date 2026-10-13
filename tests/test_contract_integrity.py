import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_frozen_hashes():
    hashes = json.loads((ROOT / 'evidence/frozen-hashes.json').read_text(encoding='utf-8'))
    for name, expected in hashes.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name


def test_exact_ten_functions_match_contract():
    source = ast.parse((ROOT / 'tests/test_fixed.py').read_text(encoding='utf-8'))
    functions = [node.name for node in source.body if isinstance(node, ast.FunctionDef)]
    contract = json.loads((ROOT / 'evidence/fixed-contract.json').read_text(encoding='utf-8'))
    assert functions == [check['function'] for check in contract['checks']]
    assert [c['id'] for c in contract['checks']] == [f'T{i:02}' for i in range(1, 11)]
