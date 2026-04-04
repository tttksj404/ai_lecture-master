# Day 11: Multi-turn과 AI Agent

LangChain 기반으로 Multi-turn 대화 흐름을 구성하고, ReAct 에이전트와 Multi-Agent 대표 패턴을 학습하며, Gradio로 나만의 RAG 시스템을 서비스 형태로 구현하는 과정입니다.

---

## 📁 폴더 구조

```
day11_agent/
├── 4_2(1)_LangChain에서_Multi_turn과_AI_Agent구현(Easy)_Solar.ipynb   # 메인 강의 노트북 1
├── 4_2(2)_Gradio와_나만의_RAG시스템_구현하기(Easy).ipynb              # 메인 강의 노트북 2
├── 실습/                                                                # 실습 문제
│   ├── (실습-문제) 4-2(1)_ReAct_기반_Agent_서비스_개발.ipynb
│   ├── (실습-힌트) 4-2(1)_ReAct_기반_Agent_서비스_개발.ipynb
│   ├── (실습-문제) 4-2(2)_Multi-Agent_대표_패턴_학습.ipynb
│   └── (실습-힌트) 4-2(2)_Multi-Agent_대표_패턴_학습.ipynb
└── 과제/                                                                # 과제
    ├── (과제-문제) 4-2(1)_ReAct_기반_Agent_서비스_개발.ipynb
    ├── (과제-힌트) 4-2(1)_ReAct_기반_Agent_서비스_개발.ipynb
    ├── (과제-문제) 4-2(2)_Multi-Agent_대표_패턴_학습.ipynb
    └── (과제-힌트) 4-2(2)_Multi-Agent_대표_패턴_학습.ipynb
```

---

## 📚 주요 학습 내용

### 1. 메인 강의 (`4_2(1)_LangChain에서_Multi_turn과_AI_Agent구현(Easy)_Solar.ipynb`)
- **Multi-turn 대화 관리**: 대화 이력 유지, 컨텍스트 기반 응답
- **Agent 기본 구조**: LLM + Tool + 실행 루프(Reasoning/Acting)
- **ReAct 패턴 이해**: 생각-행동-관찰(Thought/Action/Observation) 흐름
- **Tool Calling 기초**: 외부 도구 호출과 결과 반영

### 2. 메인 강의 (`4_2(2)_Gradio와_나만의_RAG시스템_구현하기(Easy).ipynb`)
- **Gradio UI 구성**: 입력/출력 컴포넌트, 인터랙션 설계
- **RAG 서비스화**: 검색-생성 파이프라인을 사용자 앱으로 연결
- **대화형 인터페이스**: 히스토리 기반 질의응답 UX
- **배포 관점 점검**: API 키 관리, 오류 처리, 기본 성능 고려

---

## 🧪 실습 (ReAct Agent + Multi-Agent 패턴)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | ReAct 에이전트 설계 | Tool 정의, 프롬프트 설계, 실행 루프 구성 |
| 2 | Multi-turn 적용 | 메모리/히스토리 반영, 맥락 유지 응답 |
| 3 | Multi-Agent 패턴 학습 | 역할 분리(Planner/Executor/Reviewer), 협업 구조 |
| 4 | 서비스 관점 검증 | 실패 케이스 점검, 응답 품질·안정성 테스트 |

**필요 패키지**: `python>=3.11`, `langchain`, `langchain-community`, `langchain-openai`, `gradio`, `python-dotenv`

---

## 📝 과제 (Agent 서비스 심화)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | ReAct 기반 서비스 개발 | 사용자 질의에 맞는 Tool 조합과 추론 루프 구현 |
| 2 | Multi-Agent 패턴 구현 | 문제 분해/실행/검증 역할 분리 및 오케스트레이션 |
| 3 | 품질 개선 | 프롬프트 튜닝, 무한 루프 방지, 오류 대응 강화 |
| 4 | 결과 평가 | 응답 정확성, 일관성, 사용자 경험 기준 점검 |

**권장 확장**: 도메인별 Tool 추가(검색, 계산, 요약 등)  
**필요 패키지**: `python>=3.11`, `langchain`, `langgraph`(선택), `gradio`, `openai`(또는 호환 API), `python-dotenv`

---

## 🎯 학습 목표

- Multi-turn 대화에서 문맥을 유지하는 에이전트 구조 설명
- ReAct 패턴으로 도구 활용형 AI Agent 구현
- Multi-Agent 대표 패턴(역할 분리·협업)의 장단점 이해
- Gradio 기반으로 에이전트/RAG를 사용자 서비스 형태로 연결
- 실습·과제를 통해 Agent 시스템의 품질 검증 루프 설계

---

## 📌 참고

- 실습·과제는 TODO 영역을 채우는 형태로 진행
- API 키는 `.env`로 관리하고 저장소 커밋에서 제외 권장
- Agent는 정확도뿐 아니라 안정성(루프 제어, 예외 처리)도 중요
- Multi-Agent는 복잡한 문제에서 유리하지만 오케스트레이션 설계가 핵심

