# 고정 검사 v1.0.0

구현 개선 전에 고정했다. 정확히 10개이며 보조 검사는 통계에서 제외한다. 앱별 환경변수를 분리한다.

| ID | 입력 | 기대 결과 | 실행 명령 | 판정 |
|---|---|---|---|---|
| T01 | APP_PLACE unset; create_app() | `"Flask instance"` | `python -m pytest tests/test_fixed.py::test_T01_service_start -v` | 모든 assertion 성공만 PASS |
| T02 | GET /api/health | `"HTTP 200"` | `python -m pytest tests/test_fixed.py::test_T02_health_status -v` | 모든 assertion 성공만 PASS |
| T03 | GET /api/health | `{"status": "ok", "service": "t05-stateless-handover"}` | `python -m pytest tests/test_fixed.py::test_T03_health_json -v` | 모든 assertion 성공만 PASS |
| T04 | GET /api/hello | `"HTTP 200"` | `python -m pytest tests/test_fixed.py::test_T04_hello_status -v` | 모든 assertion 성공만 PASS |
| T05 | GET /api/hello | `"version: string v2"` | `python -m pytest tests/test_fixed.py::test_T05_hello_version -v` | 모든 assertion 성공만 PASS |
| T06 | APP_PLACE unset; GET /api/hello | `"place: string UNKNOWN"` | `python -m pytest tests/test_fixed.py::test_T06_default_place -v` | 모든 assertion 성공만 PASS |
| T07 | APP_PLACE=DAEJEON; new app; GET /api/hello | `"place: string DAEJEON"` | `python -m pytest tests/test_fixed.py::test_T07_daejeon -v` | 모든 assertion 성공만 PASS |
| T08 | APP_PLACE=SEOUL; new app; GET /api/hello | `"place: string SEOUL"` | `python -m pytest tests/test_fixed.py::test_T08_seoul -v` | 모든 assertion 성공만 PASS |
| T09 | GET /api/info | `{"http": 200, "json": {"project": "T05 Stateless Handover Lab", "runtime": "Flask", "handover": true}}` | `python -m pytest tests/test_fixed.py::test_T09_info_contract -v` | 모든 assertion 성공만 PASS |
| T10 | GET /api/not-found | `{"http": 404, "json": {"error": "not_found"}}` | `python -m pytest tests/test_fixed.py::test_T10_not_found -v` | 모든 assertion 성공만 PASS |

해시 기준: `evidence/frozen-hashes.json`. 기대값·고정 검사·fixture는 이후 수정하지 않는다.
