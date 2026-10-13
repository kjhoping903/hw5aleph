# Session A 인수인계

## 1. 현재 상태와 목표
목표: 대화 없이 Git만으로 Flask API와 같은 검사 10개를 재현한다.
A 완료: hello v2와 앱 생성 시 APP_PLACE 처리. health/info/404 보존. baseline 7/10 → A 10/10.
시작 커밋: 940a15177e4d8927acd7bde7e7abf85f6c539bf1. URL: https://github.com/kjhoping903/hw5aleph/commit/940a15177e4d8927acd7bde7e7abf85f6c539bf1. 브랜치: t05-lab.
A 구현 커밋과 전달 커밋은 커밋 후 docs/session-a-log.md 및 외부 submission-manifest.json에 기록한다. B는 전달 커밋을 checkout한다.
미완료: Docker 실제 실행, 명령 정책에 차단된 독립 B의 재현·동일 검사·최종 비교.

## 2. 고정 검사 10개
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


A 결과는 모든 ID PASS. 원본: evidence/session-a-results.log 및 .xml. JSON: evidence/session-a-results.json.
계약 SHA256: 63e373af28d44eba0afb154dd8414d4d2435a55189c6a529956fe6b4a327857f.
검사 SHA256: b8f793b1c1efaed372c7c7af4cc363f8170cf93e0bd0c664e539aabdb46a076a. fixture SHA256: 7239b00ea4a5660db9daeff9a14b8eab2e6e35b975a813a9535d4173bb000ad9.
고정 파일과 기대값을 바꾸지 않는다. 보조 검사는 별도로 집계한다.

## 3. 환경 재현 방법
Python 3.12.12 설치 및 README의 가상환경 명령을 사용한다. Linux와 Windows 모두 requirements-dev.txt를 설치한다.
Docker 버전: 미확인(현재 PATH에 docker 없음). Compose도 미실행이다.
APP_PLACE=DAEJEON. 앱 생성 시 읽으므로 변경 후 재시작한다. 기본 UNKNOWN.
README에 Compose 실행·HTTP 요청·종료·Docker 검사 명령이 있다. Flask 개발 서버 사용.

## 4. 수정한 주요 파일
v1 시작점 대비 app.py만 기능 변경: import os, 지역값 읽기, version v2.
추가 파일: Dockerfile/compose.yaml, 보조 검사, 환경·증거·인수인계 스크립트, README와 문서.
git diff START..HEAD로 실제 변경 목록을 확인한다. 고정 검사·fixture·계약은 무변경이어야 한다.

## 5. 남은 문제 및 제한사항
첫 결과 수집기는 시작 커밋 이전의 Git 조회 오류로 JSON 생성에 실패했다. 원본 로그/XML을 보존하고 수집기만 수정했다.
기본 Python은 3.14였으므로 프로젝트 외부 작업 폴더의 격리 런타임 3.12.12로 검증했다. .venv는 제출하지 않는다.
Windows/Linux 클린 재현은 독립 B가 수행해야 한다. Docker 런타임과 CI 성공은 실제 실행 전 미실행이다.
GitHub의 기존 main은 도구 로그 등의 다른 파일을 포함한다. 이 브랜치는 별도 루트 이력이며 main을 덮어쓰지 않는다.
자격증명·환경변수 값·A 대화는 B에 전달하지 않는다. 공개 전환 및 강제 푸시 금지.

## 6. Session B 다음 행동
1. 빈 폴더에서 git clone --branch t05-lab https://github.com/kjhoping903/hw5aleph.git t05-b
2. cd t05-b 후 handover.md 읽기. A 대화는 요청하거나 사용하지 않는다.
3. git rev-parse HEAD와 제출 manifest의 전달 커밋 대조. 해당 SHA를 checkout.
4. Python 환경 생성·requirements 설치 후 python -m pytest tests/test_contract_integrity.py -v.
5. docker compose config --quiet; docker compose up --build -d (Docker 없으면 미실행 사유 기록).
6. curl 또는 curl.exe로 http://127.0.0.1:5600/api/hello 확인. 결과와 종료 코드 기록.
7. python scripts/run_tests.py --output evidence/session-b-start-results.json
8. python scripts/collect_evidence.py --result evidence/session-b-start-results.json --output evidence/session-b-start-context.json
9. python scripts/verify_handover.py 실행. docs/session-b-log.md에 실제 세션·모델·시각·호출·새 폴더·출력 기록.
10. 같은 검사 최종 실행: python scripts/run_tests.py --output evidence/session-b-results.json
11. 양쪽 해시·환경·결과 비교, 블라인드 표부터 작성. B 결과가 없으면 비교 미실행 유지.
12. 실제 변경만 git add 및 git commit, 가능하면 별도 B 브랜치 push. docker compose down.
검사 내용은 수정하지 않는다. 이미 실행된 결과 파일은 새 이름으로 보존한다.

## 7. 검증 및 측정 지표
초기 환경 조사 시각: 2026-10-13T06:54:45Z (15:54:45 KST). 첫 요청 수신 시각은 플랫폼 미제공.
A 기능 개선 시작 관측: 2026-10-13T06:57:59Z. 시작 커밋은 위 SHA.
전체 준비 시간과 A 구현 시간을 구분한다. 종료 시각은 최종 evidence/measurements.json에 기록한다.
고정 검사 결과: baseline passed 7, failed 3; A passed 10, failed/errors/skipped 0.
실행기 검사 소요시간은 결과 JSON의 perf_counter 값이며 AI 전체 작업시간과 다르다.
상한: 세션 90분·관측 가능한 사용자 요청+도구 호출 60회. 내부 호출·토큰은 unavailable.
서비스: Codex. 런타임 설명 모델 GPT-6. 플랫폼 세부 모델 표시 ID: 미확인.
문서가 포함된 자기 커밋 SHA를 같은 커밋에 넣지 않는다. 전달 커밋 URL은 커밋 후 외부 manifest에서 확정한다.

A 구현 커밋: d893086a8eb9fab4521070ca2a84fea8c7f24129. 최종 전달은 `t05-a-handover` 태그를 사용한다. B는 Clone 후 `git checkout t05-a-handover`로 정확한 전달 상태를 선택한다.

로컬 실제 HTTP 보조 검사: hello/health/info/404 4건 모두 기대 상태·JSON 일치. evidence/local-http-results.json 참조. Docker 시험과 구분한다.

최신 B 상태: 실제 독립 실행 시도는 FAIL(환경 정책 차단), 시작/최종 검사와 비교는 미실행. CLI 보고 토큰 61660으로 50000 상한 초과. 상세 기록은 docs/session-b-log.md.
