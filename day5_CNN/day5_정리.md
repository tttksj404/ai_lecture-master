# Day 5: CNN 모델과 Fine-tuning — 정리

Day 5 강의·실습·과제의 핵심 개념을 정리한 문서입니다.

---

## 1. 컴퓨터 비전(Computer Vision) 개요

### 1.1 분야 구분
- **컴퓨터 비전**: 영상/이미지를 활용하는 전체 분야
- **딥러닝**: 이미지를 활용한 Neural Network 기반 접근
- **영상처리**: 알고리즘/로직으로 이미지를 다루는 전통적 접근

---

## 2. MLP vs CNN

### 2.1 MLP (Multi-Layer Perceptron)
- 입력 features가 **모두 값(스칼라)**이다.
- 학습 목표: 출력을 잘 내는 **W, b**를 구하는 것
- 공간 구조(위치 정보)를 활용하지 않음

### 2.2 CNN (Convolutional Neural Network)
- **(입력 → Layers 통과 → 출력 → 오차 → 역전파)** 구조는 MLP와 동일
- 학습 목표: **"특징을 잘 뽑아내는 커널을 구하자"**
  - 데이터를 설명하는 **의미 있는 패턴** 학습
  - 해당 패턴을 **강조**하도록 커널이 학습
  - **위치 정보**까지 함께 반영

---

## 3. CNN 동작 원리

### 3.1 이미지 표현
- **RGB 이미지**: (C, H, W) — 채널×높이×너비
- **배치**: (N, C, H, W) — 배치 크기 포함

### 3.2 컨볼루션(Convolution)
- **커널(Kernel)**을 이미지 위에 슬라이딩
- 지역적 특징 추출 → **특징 맵(Feature Map)** 생성

### 3.3 풀링(Pooling)
- 특징 맵의 **공간 크기 축소**
- **불변성** 확보 (위치·크기 변화에 강건)

---

## 4. 패턴 인식의 역사

### 4.1 AlexNet (2012)
- **등장 배경**: 1970년대 커널 기반 영상처리 → 딥러닝 기반 사물인식 혁신
- **의의**: ImageNet 대회에서 압도적 성능, CNN 시대 개막
- **한계**: 깊은 네트워크에서 gradient vanishing 등 학습 난이도

### 4.2 ResNet (2015~)
- **해결**: **잔차 연결(Residual Connection, Skip Connection)** 도입
- 깊은 층에서도 gradient가 잘 흐르도록 설계
- ResNet-18, ResNet-50 등 다양한 깊이의 모델
- **ImageNet** 사전 학습 가중치로 전이 학습에 널리 활용

---

## 5. 전이 학습(Transfer Learning)

### 5.1 개념
- **ImageNet** 등 대규모 데이터로 사전 학습된 모델을 **새 태스크**에 활용
- 적은 데이터로도 높은 성능, 학습 시간 단축

### 5.2 Backbone과 Head
| 구분 | 역할 |
|------|------|
| **Backbone** | conv layers — 특징 추출 |
| **Head** | fc layer — 태스크별 분류 출력 |

### 5.3 Linear Probing vs Fine-tuning
| 방식 | 설명 | 적합한 경우 |
|------|------|-------------|
| **Linear Probing** | Backbone **동결**, 분류층(fc)만 학습 | 적은 데이터, 빠른 적응 |
| **Fine-tuning** | 전체 또는 **일부 레이어** 해제 후 학습 | 성능 극대화, 학습률 낮게(0.0001~0.001) |
| **Partial Fine-tuning** | Backbone 일부(layer4 등) + fc 학습 | 도메인 차이 보정 |

### 5.4 동결(Freezing)
- `requires_grad=False` → 해당 파라미터는 **업데이트 안 함**
- 사전 학습 지식 보존, 과적합 방지

---

## 6. 데이터 증강 & 학습률 스케줄러

### 6.1 데이터 증강(Augmentation)
- **RandomCrop**, **RandomHorizontalFlip** 등
- 학습 데이터 다양성 확보 → **과적합 방지**, **일반화** 향상

### 6.2 학습률 스케줄러
- **StepLR**: 주기적으로 학습률 감소
- **ReduceLROnPlateau**: 성능 정체 시 학습률 감소

---

## 7. Vision Transformer (ViT)

- 이미지를 **패치(Patch)**로 분할
- **Transformer 인코더**로 처리
- CNN 대비 글로벌한 관계 학습 가능

---
