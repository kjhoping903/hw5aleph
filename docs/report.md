# T05 Stateless Handover Lab — Session A 보고서

## 1. 프로젝트 개요
대화 대신 Git·검사·인수인계 문서를 기준으로 Flask 실습을 재개한다. Python 3.12.12와 Flask 3.1.2, pytest 8.4.2를 사용했다.
기존 BYTE BACK과 hw5aleph main은 보존하고 새 t05-lab 브랜치에 독립 프로젝트 이력을 만들었다.

## 2. 검사 10개
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


A baseline 7/10 (T05·T07·T08 FAIL), A 최종 모든 항목 PASS 10/10. B 시작/최종은 미실행.
검사 SHA256: b8f793b1c1efaed372c7c7af4cc363f8170cf93e0bd0c664e539aabdb46a076a.
계약 SHA256: 63e373af28d44eba0afb154dd8414d4d2435a55189c6a529956fe6b4a327857f.
fixture까지 포함한 불변성 검사 2개 PASS. 앱 초기화 시 환경변수 snapshot 보조 검사 1개 PASS. 보조 검사는 고정 10개 집계에 포함하지 않는다.

## 3. Session A 작업
최초 관측 2026-10-13T06:54:45Z, 기능 개선 시작 관측 2026-10-13T06:57:59Z.
시작 커밋 [940a15177e4d8927acd7bde7e7abf85f6c539bf1](https://github.com/kjhoping903/hw5aleph/commit/940a15177e4d8927acd7bde7e7abf85f6c539bf1). v1·고정 검사·baseline을 실제 커밋한 뒤 hello v2와 APP_PLACE를 구현했다.
실행 결과: evidence/baseline-results.json, evidence/session-a-results.json. 로그/XML도 보존했다.
최종 커밋은 자기참조를 피하여 커밋 후 외부 submission-manifest.json에 확정한다. 작업시간·관측 호출은 evidence/measurements.json에 기록한다.
서비스 Codex, 런타임 모델 설명 GPT-6, 플랫폼 상세 표시 ID 미확인. 내부 호출·토큰 미제공.

## 4. 인수인계
루트 handover.md에 현재 상태, 검사, 환경, 변경 파일, 제한, B 다음 행동, 측정의 7항목을 작성했다.
독립 B는 공개 저장소와 이 문서만 받아 빈 폴더에 Clone하고 같은 전달 커밋을 사용한다. A의 대화 전문은 전달하지 않는다.

## 5. Session B
실제 독립 세션 결과는 아직 미실행. Codex CLI 비대화형 실행과 로그인 가능 여부를 조사했다.
공식 [비대화형 실행 문서](https://learn.chatgpt.com/docs/non-interactive-mode)와 로컬 도움말을 확인했다. 로그인 성공만으로 B 재현 성공을 주장하지 않는다.
실행이 불가능하면 docs/session-b-prompt.md를 새 실제 세션에 제공한다. B 로그·결과는 실제 실행 후에만 채운다.

## 6. A/B 비교
미실행. B 결과와 동일 해시·환경 증거가 모이면 docs/comparison.md의 사전 기준에 따라 X/Y 블라인드 표를 먼저 작성한다.
검사 통과·실패·오류·시간·요청·토큰·Git 상태·수정 파일·환경 재현을 비교한다. 승패를 만들기 위해 값을 바꾸지 않는다.

## 7. 실패 및 한계
v1의 T05/T07/T08 실패를 그대로 보존했다. 첫 결과 수집기의 Git 조회 오류를 수정했으며 테스트를 변경하지 않았다.
Docker 명령이 없어 Compose와 컨테이너 HTTP는 미실행이다. 로컬 Python test_client 통과와 구분한다.
CI 워크플로는 구성 여부와 실제 실행 성공을 구분한다. Linux와 클린 환경 재현은 B가 확인해야 한다.
외부 계정·인증·엔진 상태는 Git만으로 보장하지 않는다. 본 프로젝트는 DB·회원가입·외부 API를 사용하지 않는다.
공개 접근은 인증 없는 요청의 증거를 확인해야 하며 Git push 성공만으로 공개 조건을 통과 처리하지 않는다.

## 8. 실행 안내
README의 Windows/Linux/Python/Docker 명령을 따른다. `python -m pytest tests/test_fixed.py -v`가 고정 검사 10개다.
`python scripts/verify_environment.py`, `python scripts/verify_handover.py`로 환경·인수인계도 확인한다. 종료는 Ctrl+C 또는 docker compose down.

## 9. 제출 정보
공개 결과물과 소스 URL은 같은 최종 전체 SHA로 외부 manifest에서 확정한다. 아직 업로드하지 않은 URL을 공개 성공이라고 쓰지 않는다.
위치: 이 docs/report.md 및 커밋 후 외부 제출 manifest.
행동: Clone/전달 SHA checkout → requirements-dev 설치 → 고정 pytest 실행.
통과 모습: 실제 A 10 passed, FAIL/ERROR/SKIP 0. B는 미실행.
안 될 때 모습: pytest 실패/수집 오류 또는 해시 불일치가 나오며 0이 아닌 종료 코드. Docker 없으면 관련 시험 미실행.

1. AI에게 맡긴 일: 새 Flask 프로젝트, 고정 검사·실행 증거, Docker 설정과 인수인계 문서 작성.
2. 직접 판단한 일: 사용자가 새 Flask 통합 범위와 저장 대상 hw5aleph를 지정했다.
3. AI 제안을 따르지 않은 일: 사용자가 BYTE BACK CLI 제안 대신 새 Flask 통합 프롬프트를 제공했다.

### 평가 기준 상태
상세 문구가 제공되지 않아 식별자만으로 PASS를 추정하지 않는다.
| 기준 | 상태 | 사유 |
|---|---|---|
| T05-C01 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C02 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C03 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C04 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C05 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C06 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C07 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C08 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C09 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C10 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C11 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C12 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C13 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C14 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C15 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C16 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C17 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C18 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C19 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C20 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C21 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C22 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C23 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C24 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C25 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C26 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C27 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C28 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C29 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C30 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C37 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C38 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C39 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C50 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C51 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C52 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |
| T05-C53 | 미확인 | 상세 기준 미확인; 식별자만 제공됨 |

