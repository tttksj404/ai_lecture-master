# Day 7: 토큰화와 임베딩

자연어를 모델 입력으로 변환하는 토큰화(Tokenization)와 임베딩(Embedding)을 학습하고, 시퀀스 모델(RNN/LSTM/Attention/Transformer)의 발전 과정을 이해하는 과정입니다.

---

## 📁 폴더 구조

```
day7_embeddings/
├── 2_1_토큰화_임베딩_(Easy).ipynb   # 메인 강의 노트북
├── 실습/                              # 실습 문제
│   ├── (실습-문제) 2-1_토큰화,임베딩_실습.ipynb
│   └── (실습-힌트) 2-1_토큰화,임베딩_실습.ipynb
└── 과제/                              # 과제
    ├── (과제-문제) 2-1_토큰화,임베딩_심화_과제.ipynb
    └── (과제-힌트) 2-1_토큰화,임베딩_심화_과제.ipynb
```

---

## 📚 주요 학습 내용

### 1. 메인 강의 (`2_1_토큰화_임베딩_(Easy).ipynb`)
- **토크나이저**: 문장을 토큰 단위로 분할하고 수(Index)로 변환하는 도구
- **토큰화 알고리즘**: WordPiece, Byte-Level BPE
- **임베딩**: 토큰 ID를 고정 차원 벡터로 매핑
- **허깅페이스(Hugging Face)**: transformers 라이브러리로 사전 학습 모델 활용

---

## 🧪 실습 (토큰화·임베딩·시퀀스 모델)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 토크나이저·임베딩 | NSMC로 WordPiece 학습, 토큰 ID 변환, nn.Embedding 조회 |
| 2 | RNN/LSTM | RNNEncoder·RNNDecoder, Encoder-Decoder 구조, Seq2Seq |
| 3 | Attention | Luong Attention, Score·Context Vector, AttentionDecoder |
| 4 | Huggingface | Helsinki-NLP 번역 모델, Seq2Seq 추론 |
| 5 | 아키텍처별 모델 | BERT(Encoder-only), GPT(Decoder-only) 추론 |

**데이터셋**: NSMC (Naver Sentiment Movie Corpus, 약 20만 리뷰)  
**필요 패키지**: `python>=3.11`, `torch`, `transformers`, `tokenizers`, `sentencepiece`, `sacremoses`, `numpy`, `pandas`

---

## 📝 과제 (토큰화·임베딩 심화)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 토큰화·임베딩 심화 | 토크나이저 학습, 토큰 ID 시퀀스, nn.Embedding |
| 2 | 시퀀스 모델 | RNN/LSTM Encoder-Decoder, Attention, Seq2Seq |
| 3 | Huggingface 활용 | 사전 학습 모델 추론, BERT·GPT 아키텍처 이해 |

**필요 패키지**: `python>=3.11`, `torch`, `transformers`, `tokenizers`, `numpy`, `pandas`

---

## 🎯 학습 목표

- 토크나이저·토큰화의 개념과 필요성 설명
- WordPiece·BPE 기반 토크나이저 학습 및 사용
- nn.Embedding으로 토큰을 벡터로 변환
- RNN/LSTM의 순차 처리 방식과 Encoder-Decoder 구조 이해
- Attention 메커니즘의 작동 원리와 효과 설명
- BERT(Encoder-only)·GPT(Decoder-only)·Seq2Seq 아키텍처 구분

---

## 📌 참고

- 실습·과제는 TODO 영역을 채우는 형태로 진행
- 강의(토큰화·임베딩) → 실습(Seq2Seq·Attention) → 과제(심화) 순으로 진행 권장
- 허깅페이스 모델 다운로드 시 인터넷 연결 필요
