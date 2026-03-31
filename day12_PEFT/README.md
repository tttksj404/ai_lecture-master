# Day 12: 효율적인 Fine-tuning (PEFT)

대형 언어 모델을 전부 재학습하지 않고, LoRA/QLoRA 같은 기법으로 적은 자원으로 빠르게 튜닝하는 방법을 학습하는 과정입니다.

---

## 📁 폴더 구조

```
day12_PEFT/
├── 5_1_효율적인_Fine_tuning_PEFT(Easy).ipynb              # 메인 강의 노트북
├── 실습/                                                   # 실습 문제
│   ├── (실습-문제) 5-1_PEFT_파라미터_효율적_튜닝.ipynb
│   └── (실습-힌트) 5-1_PEFT_파라미터_효율적_튜닝.ipynb
└── 과제/                                                   # 과제
    ├── (과제-문제) 5-1_PEFT_파라미터_효율적_튜닝.ipynb
    └── (과제-힌트) 5-1_PEFT_파라미터_효율적_튜닝.ipynb
```

---

## 📚 주요 학습 내용

### 1. 메인 강의 (`5_1_효율적인_Fine_tuning_PEFT(Easy).ipynb`)
- **PEFT 개념**: Full Fine-tuning 대비 파라미터 효율적으로 학습하는 이유
- **LoRA 원리**: 저랭크 행렬 분해로 업데이트 파라미터 수를 줄이는 방식
- **QLoRA 개념**: 양자화(4-bit) + LoRA 결합으로 메모리 절감
- **Unsloth 활용**: 효율적 학습/추론을 위한 실무형 라이브러리 사용

### 2. 실습·과제 공통 핵심
- **메모리 관점 비교**: Full Fine-tuning vs PEFT 메모리/연산량 비교
- **데이터 전처리**: Chat Template 적용, Label Masking 설계
- **학습 설정 튜닝**: LoRA rank, alpha, dropout, 학습률 등의 영향 확인
- **결과 점검**: 추론 품질, 학습 안정성, 자원 사용량 관점의 평가

---

## 🧪 실습 (PEFT/QLoRA 적용)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 환경 설정 및 모델 로드 | Unsloth 기반 4-bit 모델 로드, 토크나이저 설정 |
| 2 | Full FT 한계 체감 | 비트 정밀도별 메모리 요구량 계산·시각화 |
| 3 | LoRA 원리 점검 | PEFT 필요성, LoRA 하이퍼파라미터 이해 |
| 4 | LoRA 학습 실행 | Chat Template 적용 후 학습 루프 구성 |
| 5 | 결과 확인 | 응답 품질과 메모리/속도 관점 비교 |

**필요 패키지**: `python>=3.10`, `torch`, `transformers`, `datasets`, `peft`, `trl`, `bitsandbytes`, `accelerate`, `unsloth`

---

## 📝 과제 (Text-to-SQL + PEFT 심화)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 데이터셋 EDA | ko_text2sql 데이터 길이·분포 확인, max length 결정 |
| 2 | 모델/토크나이저 준비 | HuggingFace 모델 로드, 학습 정밀도 설정 |
| 3 | 데이터 전처리 | Chat Template 변환, instruction 구간 Label Masking |
| 4 | LoRA 학습 | `LoraConfig` 및 `SFTTrainer` 기반 학습 |
| 5 | 성능 점검 | 예측 SQL 품질 확인, 실패 케이스 분석 |

**권장 패키지**: `python>=3.10`, `torch`, `transformers`, `datasets`, `peft`, `trl`, `pandas`

---

## 🎯 학습 목표

- Full Fine-tuning이 왜 비싼지 메모리 관점에서 설명
- PEFT/LoRA/QLoRA의 핵심 차이와 적용 상황 구분
- Chat Template + Label Masking 기반 학습 데이터 구성
- 제한된 GPU 환경에서 실용적인 Fine-tuning 파이프라인 구현
- 자원 효율성과 출력 품질을 함께 고려한 튜닝 전략 수립

---

## 📌 참고

- 실습·과제는 TODO 영역을 채우는 형태로 진행
- GPU VRAM이 작을수록 QLoRA(4-bit) 접근이 유리
- LoRA 하이퍼파라미터(`r`, `lora_alpha`, `lora_dropout`)는 성능/안정성에 직접 영향
- 학습 결과는 정답률뿐 아니라 추론 일관성, 메모리 사용량도 함께 점검 권장
