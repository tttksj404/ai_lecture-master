# Day 10: LangChain과 RAG

LangChain 기반으로 RAG(Retrieval-Augmented Generation) 파이프라인을 구성하고, 검색 기반 고객지원 AI 에이전트를 구현하는 과정입니다.

---

## 📁 폴더 구조

```
day10_rag/
├── 4_1_Langchain과_RAG(Easy)_Solar.ipynb                         # 메인 강의 노트북
├── 실습/                                                          # 실습 문제
│   ├── (실습-문제) 4-1_RAG_기반_Customer_Service_AI_에이전트_개발.ipynb
│   └── (실습-힌트) 4-1_RAG_기반_Customer_Service_AI_에이전트_개발.ipynb
└── 과제/                                                          # 과제
    ├── (과제-문제) 4-1_RAG_기반_Customer_Service_AI_에이전트_개발.ipynb
    └── (과제-힌트) 4-1_RAG_기반_Customer_Service_AI_에이전트_개발.ipynb
```

---

## 📚 주요 학습 내용

### 1. 메인 강의 (`4_1_Langchain과_RAG(Easy)_Solar.ipynb`)
- **RAG 개념**: LLM 생성에 외부 지식 검색 결과를 결합
- **LangChain 구성 요소**: 문서 로딩, 분할, 임베딩, 벡터스토어, 리트리버, 체인
- **검색 품질**: chunk 전략, top-k, 관련도 기반 검색 튜닝
- **응답 신뢰성**: 근거 기반 답변, 환각(hallucination) 완화

---

## 🧪 실습 (RAG 기반 고객지원 에이전트)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 문서 수집·전처리 | 고객지원 FAQ/정책 문서 로드, 정제 |
| 2 | Chunking·임베딩 | 문서 분할 전략, 임베딩 생성 |
| 3 | 벡터 검색 | 벡터스토어 구축, 유사도 검색, top-k 실험 |
| 4 | RAG 체인 구성 | Retriever + LLM 결합, 프롬프트 템플릿 적용 |
| 5 | 응답 검증 | 근거 포함 답변, 실패 케이스 점검 |

**필요 패키지**: `python>=3.11`, `langchain`, `langchain-community`, `langchain-openai`, `faiss-cpu`(또는 `chromadb`), `pandas`

---

## 📝 과제 (RAG 에이전트 심화)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 도메인 확장 | 새로운 업무 문서셋으로 지식베이스 확장 |
| 2 | 검색 개선 | chunk size/overlap, top-k, 임계값 튜닝 |
| 3 | 프롬프트 개선 | 근거 우선 응답, 답변 형식 통일 |
| 4 | 평가 루프 | 정답률/근거충실도/무응답 정책 점검 |

**권장 데이터**: 고객지원 FAQ, 운영 정책 문서, 서비스 가이드  
**필요 패키지**: `python>=3.11`, `langchain`, `langchain-openai`, `faiss-cpu`(또는 `chromadb`), `numpy`, `pandas`

---

## 🎯 학습 목표

- RAG 파이프라인(문서→임베딩→검색→생성) 전체 흐름 설명
- LangChain으로 Retriever-LLM 체인 구현
- 검색 품질(top-k, chunking)과 응답 품질의 관계 이해
- 근거 기반 응답으로 환각을 줄이는 실무적 접근 습득
- 고객지원 시나리오에서 RAG 에이전트 설계·검증

---

## 📌 참고

- 실습·과제는 TODO 영역을 채우는 형태로 진행
- 벡터스토어는 환경에 맞게 `FAISS` 또는 `Chroma` 중 선택
- API 키는 `.env`로 관리하고 저장소 커밋에서 제외 권장
- RAG 성능은 모델 성능뿐 아니라 데이터 품질/분할 전략 영향을 크게 받음

