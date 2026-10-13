# 독립 Session B 실행 기록

실제 새 CLI 세션을 두 번 시도했다. resume/fork 없이 새 프로세스, --ephemeral, --ignore-user-config를 사용했다. A 대화는 stdin에 전달하지 않았다.
첫 시도: gpt-5.3-codex를 요청했지만 ChatGPT 계정에서 지원하지 않는 모델이라는 HTTP 400으로 시작 전에 실패했다.
두 번째 시도: 계정 기본 모델, 새 thread 01a1341f-9699-75f1-8136-4a85ff282f04. actual 모델 표시 ID는 검증 불가이며 A와 다른 모델을 사용했다고 주장하지 않는다.
새 작업 폴더: t05-independent-b-2. B 첫 요청에는 저장소 URL, handover 읽기 지시, 같은 기능 목표와 상한만 포함했다.
B 명령 실행은 blocked by policy로 거절됐다. 웹 handover 조회도 당시 cache miss로 실패했다. 이때 저장소 공개 전환과 B 조회가 겹쳤으므로 접근 실패를 공개 상태의 최종 증거로 사용하지 않는다.
Clone SHA·검사 해시·환경 재현·시작/최종 고정 검사·수정·커밋·푸시: 미실행.
시작/종료·실측 경과시간: evidence/b-attempt-2.supervisor.json. 실제 원본 events와 stderr 보존.
관측 도구: JSON events의 web_search 2회, stderr로 확인한 차단된 exec 1회. 합계 3회. 내부 호출 수는 unavailable.
B 자체 응답의 사용자 요청 2회 표시는 외부 supervisor가 보낸 최초 stdin 1회와 불일치하므로 실제 측정값으로 채택하지 않는다.
실제 CLI usage는 input_tokens 60958 (cached 57344 포함), output_tokens 702. 총 61660으로 50000 상한을 초과했다. usage는 turn 완료 후 제공되어 사전에 제어할 수 없었다. 이 초과를 숨기거나 추정값으로 바꾸지 않는다.
전체 작업시간과 토큰 제한을 지켰다고 일괄 PASS하지 않는다. actual B 검사가 없으므로 A/B 통과율과 블라인드 우열 비교는 미실행이다.
재개는 실행/쓰기 권한이 있는 새로운 실제 AI 세션에서 docs/session-b-prompt.md만 제공해 수행해야 한다.
