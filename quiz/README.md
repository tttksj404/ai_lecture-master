# AI 강의 퀴즈

`quiz.html`이 `quiz_data.json`을 읽어 퀴즈를 실행합니다.

## 실행 방법

### Live Server (VS Code 확장)

1. **설치**: VS Code 확장 탭에서 `Live Server` 검색 후 설치 (작성자: Ritwick Dey)
2. **실행**: `quiz.html` 파일에서 우클릭 → **Open with Live Server** 선택
3. 브라우저가 자동으로 열리며 퀴즈 실행

### 문제풀이 시 참고

- `단답형 문제는 대부분 오답으로 나옵니다`
  - 해설과 함께 참고해서 학습용으로만 써주세요!


### 참고

- `quiz.html` 더블클릭(file://)은 JSON 로드가 차단되어 동작하지 않음

## 기능

1. **페이지 접근 시**: 풀고자 하는 단원 선택 (Day 1 / Day 2 / Day 3 / Day 4 / Day 5 / Day 6 / Day 7 / Day 8)
2. **단원 선택 시**: 해당 단원의 문제풀이 시작
3. **진행 중**: 맞힌 개수, 정답률 실시간 표시
4. **완료 후**: 최종 점수 및 피드백

## 파일 구조

```
quiz/
├── quiz.html         # 퀴즈 앱 (quiz_data.json 로드)
├── quiz_data.json    # 퀴즈 데이터 (문제, 정답, 해설)
└── README.md
```
