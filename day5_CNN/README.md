# Day 5: CNN 모델과 Fine-tuning

컨볼루션 신경망(CNN)의 동작 원리와 전이 학습(Transfer Learning), Fine-tuning을 학습하는 과정입니다.

---

## 📁 폴더 구조

```
day5_CNN/
├── 3_1_CNN_모델과_Fine_tuning_(Easy).ipynb   # 메인 강의 노트북
├── 실습/                                     # 실습 문제
│   ├── (실습-문제) 3-1_Transfer Learning 기반의 CNN 모델 학습.ipynb
│   └── (실습-힌트) 3-1_Transfer Learning 기반의 CNN 모델 학습.ipynb
└── 과제/                                     # 과제
    ├── (과제-문제) 3-1_Transfer Learning 기반의 CNN 모델 학습.ipynb
    └── (과제-힌트) 3-1_Transfer Learning 기반의 CNN 모델 학습.ipynb
```

---

## 📚 주요 학습 내용

### 1. 메인 강의 (`3_1_CNN_모델과_Fine_tuning_(Easy).ipynb`)
- **CNN 역사**: 영상처리·패턴인식, AlexNet 등장, 사물인식 발전
- **CNN 동작 원리**: RGB 이미지 표현, 컨볼루션, 풀링, 배치 처리
- **전이 학습**: 사전 학습 모델 활용, Linear Probing, Fine-tuning

---

## 🧪 실습 (Transfer Learning 기반 CNN)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | Linear Probing | ResNet-18 특징 추출부 동결, 분류층만 학습 |
| 2 | Fine-tuning & Augmentation | 데이터 증강, 전체 모델 학습, 학습률 스케줄러 |
| 3 | Vision Transformer | HuggingFace ViT 모델로 이미지 분류 추론 |

**데이터셋**: CIFAR-10  
**필요 패키지**: `python>=3.11`, `torch`, `torchvision`, `transformers`, `datasets`

---

## 📝 과제 (Transfer Learning 심화)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 데이터 준비·전처리 | Flowers102 로드, 정규화, train/val/test 구성 |
| 2 | Partial Fine-tuning | Backbone(layer4)+Head(fc) 학습, Optimizer/Scheduler 조합 비교 |

**데이터셋**: Flowers102  
**필요 패키지**: `python>=3.11`, `torch`, `torchvision`, `numpy`, `matplotlib`, `tqdm`

---

## 🎯 학습 목표

- CNN의 컨볼루션·풀링 동작 원리 이해
- 전이 학습(Transfer Learning) 개념과 Linear Probing vs Fine-tuning 차이
- ResNet-18을 활용한 이미지 분류 전이 학습 구현
- 데이터 증강, 학습률 스케줄러로 성능 개선
- Vision Transformer(ViT) 추론 활용

---

## 📌 참고

- 실습·과제는 TODO 영역을 채우는 형태로 진행
- CIFAR-10은 32×32 저해상도 — 실무에서는 고해상도 데이터 사용
- ViT 사용 시 `transformers==4.57.1` 버전 고정
