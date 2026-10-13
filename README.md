# T05 Stateless Handover Lab

## 1. 프로젝트 소개
작은 Flask API를 Git과 인수인계 문서만으로 재현하는 실습이다. 기존 BYTE BACK과 hw5aleph main은 보존한다. 새 프로젝트의 독립 이력은 `t05-lab` 브랜치에 저장한다.

## 2. T05 실습 목적
대화 밖에 코드·검사·환경·남은 일을 저장한다. 외부 계정, Docker 설치, 서비스의 실제 상태는 Git만으로 보장하지 않는다.

## 3. Flask API 설명
GET /api/hello: message=Hello, version=v2, place=APP_PLACE 또는 UNKNOWN.
GET /api/health: status=ok, service=t05-stateless-handover.
GET /api/info: project=T05 Stateless Handover Lab, runtime=Flask, handover=true.
없는 경로: HTTP 404와 {"error":"not_found"}.
APP_PLACE는 앱 생성 때 읽는다. 실행 중 변경은 앱 재시작 후 반영된다. 빈 문자열은 설정된 값으로 취급한다.

## 4. 기술 스택
Python 3.12.12, Flask 3.1.2, pytest 8.4.2. 전이 의존성도 requirements 파일에 고정했다.
Dockerfile은 Python 3.12.12 slim-bookworm을 사용한다. 이미지 digest 검증 상태는 evidence/remote-preflight.json 참조.
Flask 개발 서버를 사용하는 로컬 실습이며 운영 배포 구성은 아니다.

## 5. 폴더 구조
app.py: API. tests/: 고정 10개 및 별도 보조 검사. scripts/: 실행·환경·증거·인수인계 검사.
docs/: 계획·A/B 로그·비교·보고서. evidence/: JSON 결과와 실제 pytest 로그/XML.

## 6. 실행 방법
Python 3.12가 설치되어 있어야 한다. Windows PowerShell:
```powershell
git clone --branch t05-lab https://github.com/kjhoping903/hw5aleph.git t05-reproduction
cd t05-reproduction
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
$env:APP_PLACE = 'DAEJEON'
.\.venv\Scripts\python.exe -m flask --app app:create_app run --host 127.0.0.1 --port 5600
```
Linux:
```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
APP_PLACE=DAEJEON python -m flask --app app:create_app run --host 127.0.0.1 --port 5600
```
다른 터미널에서 Windows는 `curl.exe http://127.0.0.1:5600/api/hello`, Linux는 `curl http://127.0.0.1:5600/api/hello`로 확인한다. 서버는 Ctrl+C로 종료한다.
Docker가 설치된 환경:
```bash
docker compose config --quiet
docker compose up --build -d
docker compose ps
docker compose logs --tail=50 web
docker compose down
```
외부 호스트 포트는 127.0.0.1:5600이다. .env.example을 .env로 복사해 지역값을 설정할 수 있다. 실제 .env는 Git 제외.
Docker만으로 검사:
```bash
docker build --target test -t t05-tests .
docker run --rm t05-tests
```
Docker 이미지의 pytest 출력은 보조 Docker 실행 증거로 별도 보존한다.

## 7. 고정 검사 10개
`docs/test-plan.md`와 `evidence/fixed-contract.json`에 입력·기대·명령·판정을 저장했다.
가상환경 활성화 후:
```bash
python -m pytest tests/test_fixed.py -v
python -m pytest tests/test_contract_integrity.py tests/test_initialization.py -v
```
첫 명령은 고정 10개만, 두 번째는 보조 3개만 실행한다.

## 8. AI A/B 인수인계 방식
B는 새 실제 세션과 빈 작업 디렉터리를 사용한다. A 대화를 전달하지 않는다. `handover.md`부터 읽고 정확한 A 전달 커밋을 checkout한다.
실행 시 상한 90분, 관측 가능한 사용자 요청+도구 호출 합계 60회. 내부 호출과 토큰은 미제공이면 unavailable.

## 9. 결과 확인
baseline 7/10, A 최종 10/10. 실제 B는 별도 실행 후에만 집계한다.
JSON은 evidence/에 있다. 실행기를 다시 쓸 때 기존 실행 증거를 덮어쓰지 않도록 새 출력 이름을 사용한다. not_run 템플릿만 실행 결과로 교체할 수 있다.

## 10. 공개 보고서
[보고서](docs/report.md). 고정 커밋 링크는 커밋·푸시 후 외부 제출 manifest에 확정한다. 시작 커밋: 940a15177e4d8927acd7bde7e7abf85f6c539bf1.
설계 근거: [Flask factory](https://flask.palletsprojects.com/en/stable/patterns/appfactories/), [pytest plugins](https://docs.pytest.org/en/stable/how-to/writing_plugins.html).
