# Day 8: AI를 이용한 데이터 생성

LLM을 활용한 소량·대량 텍스트 데이터 생성, 데이터 증강, 합성 데이터(Synthetic Data) 생성 및 LLM as Judge 품질 평가를 학습하는 과정입니다.

---

## 📁 폴더 구조

```
day8_data_synthetic/
├── 2_2_AI를_이용한_데이터_생성법(Easy)_Solar.ipynb   # 메인 강의 노트북
├── 실습/                                            # 실습 문제
│   ├── (실습-문제) 2-2_합성_데이터_실습.ipynb
│   └── (실습-힌트) 2-2_합성_데이터_실습.ipynb
└── 과제/                                            # 과제
    ├── (과제-문제) 2-2_합성_데이터_생성_과제.ipynb
    └── (과제-힌트) 2-2_합성_데이터_생성_과제.ipynb
```

---

## 📚 주요 학습 내용

### 1. 메인 강의 (`2_2_AI를_이용한_데이터_생성법(Easy)_Solar.ipynb`)
- **소량 텍스트 생성**: LLM에게 예시를 주고 새로운 데이터 생성
- **대량 데이터 생성**: 소형 모델로 생성, LLM as Judge로 필터링
- **데이터 증강 vs 합성 데이터**: 개념 이해
- **이미지 데이터 증강**: 기초 개념

---

## 🧪 실습 (합성 데이터 생성·평가)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 환경 설정·API 호출 | 환경 변수, OpenAI 호환 API, LLM 호출 함수 |
| 2 | 프롬프팅 기법 비교 | Zero-shot, Few-shot, Chain-of-Thought(CoT) |
| 3 | 구조화된 합성 데이터 | JSON 형식 지정, Structured Output, temperature |
| 4 | LLM as Judge | 품질 자동 평가, 평가 기준, 필터링 |

**필요 패키지**: `python>=3.11`, `pandas`, `openai`, `python-dotenv`

---

## 📝 과제 (합성 데이터 생성 심화)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 프롬프팅 기법 비교 | Zero-shot, Few-shot, CoT로 번역 품질 비교 |
| 2 | 데이터 증강 | 페르소나 기반 다양한 스타일 한국어 데이터 생성 |
| 3 | LLM as Judge | 의미 보존 평가, 점수 기반 필터링 |

**데이터셋**: sql-create-context (Text-to-SQL)  
**필요 패키지**: `python>=3.11`, `datasets`, `openai`, `python-dotenv`

---

## 🎯 학습 목표

- 환경 변수로 API 키를 안전하게 관리하고 LLM 호출
- Zero-shot, Few-shot, CoT 프롬프팅 기법의 특성 이해 및 적용
- 구조화된(JSON) 합성 데이터 생성
- LLM as Judge로 생성 데이터 품질 자동 평가·필터링
- 합성 데이터 생성 → 평가 → 선별 파이프라인 구축

---

## 📌 참고

- 실습·과제는 TODO 영역을 채우는 형태로 진행
- API 키는 `.env` 파일에 저장, `.gitignore`에 포함 권장
- Upstage API 등 OpenAI 호환 API 사용
