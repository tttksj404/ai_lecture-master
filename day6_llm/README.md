# Day 6: 파운데이션에서 멀티모달까지, LLM 모델의 진화

파운데이션 모델, 멀티모달(이미지 생성·평가), 디퓨전·CLIP·전이학습을 학습하는 과정입니다.

---

## 📁 폴더 구조

```
day6_llm/
├── 3_2_파운데이션에서_멀티모달까지,_LLM_모델의_진화(Easy).ipynb   # 메인 강의 노트북
├── 실습/                                                         # 실습 문제
│   ├── (실습-문제) 3-2_이미지 생성 및 평가와 모델 학습.ipynb
│   └── (실습-힌트) 3-2_이미지 생성 및 평가와 모델 학습.ipynb
└── 과제/                                                         # 과제
    ├── (과제-문제) 3-2_이미지 생성 및 평가와 모델 학습.ipynb
    └── (과제-힌트) 3-2_이미지 생성 및 평가와 모델 학습.ipynb
```

---

## 📚 주요 학습 내용

### 1. 메인 강의 (`3_2_파운데이션에서_멀티모달까지,_LLM_모델의_진화(Easy).ipynb`)
- **파운데이션 모델**: 대규모 사전 학습, 다양한 태스크 적응
- **멀티모달**: 이미지·텍스트 결합, 디퓨전·CLIP
- **이미지 생성·평가**: Text-to-Image, 이미지-텍스트 유사도

---

## 🧪 실습 (이미지 생성 및 평가와 모델 학습)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 텍스트-투-이미지 생성 | SANA 디퓨전 모델, 프롬프트 엔지니어링 |
| 2 | CLIP 이미지 평가 | 이미지-텍스트 유사도, 멀티모달 평가 |
| 3 | ResNet-50 분류 비교 | CLIP vs CNN 분류 결과 비교 |
| 4 | ResNet-18 전이학습 | 합성 데이터로 리니어 프로빙 |

**필요 패키지**: `python>=3.11`, `torch`, `torchvision`, `transformers`, `diffusers`, `accelerate`, `Pillow`

---

## 📝 과제 (이미지 생성·평가 심화)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 0 | Inference API | HuggingFace API로 이미지 생성 이해 |
| 1 | Text-to-Image | Stable Diffusion, Positive/Negative 프롬프트 |
| 2 | CLIP 평가 | 이미지-텍스트 유사도 측정 |
| 3 | ResNet-50 비교 | CLIP vs CNN 비교 분석 |
| 4 | ResNet-18 Fine-tuning | 합성 데이터셋 구축·학습 |
| 5 | (선택) Knowledge Distillation | Teacher-Student 지식 증류 |

**필요 패키지**: `python>=3.11`, `torch`, `torchvision`, `transformers`, `diffusers`, `accelerate`, `Pillow`

---

## 🎯 학습 목표

- 디퓨전 모델(SANA, Stable Diffusion)로 텍스트 기반 이미지 생성
- CLIP으로 이미지-텍스트 유사도 측정·해석
- CLIP vs ResNet 분류·평가 특성 차이 이해
- 합성 데이터로 전이학습(리니어 프로빙·Fine-tuning) 구현
- (선택) Knowledge Distillation 기초

---

## 📌 참고

- 실습·과제는 TODO 영역을 채우는 형태로 진행
- SANA, Stable Diffusion은 GPU 권장(메모리 부족 시 `enable_model_cpu_offload()`)
- day5_CNN(전이학습) 선행 학습 권장
