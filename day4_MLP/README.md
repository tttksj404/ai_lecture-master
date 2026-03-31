# Day 4: 신경망과 MLP

신경망(Neural Network) 개념과 MLP(Multi-Layer Perceptron)를 PyTorch로 구현하는 과정입니다.

---

## 📁 폴더 구조

```
day4_MLP/
├── 1_2_신경망(Neural_Network)과_MLP_(Easy).ipynb   # 메인 강의 노트북
├── 실습/                                            # 실습 문제
│   ├── (실습-문제) 1-2_MLP 구현.ipynb
│   └── (실습-힌트) 1-2_MLP 구현.ipynb
└── 과제/                                            # 과제
    ├── (과제-문제) 1-2_간단한 Perceptron 구현.ipynb
    └── (과제-힌트) 1-2_간단한 Perceptron 구현.ipynb
```

---

## 📚 주요 학습 내용

### 1. 메인 강의 (`1_2_신경망(Neural_Network)과_MLP_(Easy).ipynb`)
- **신경망 개념**: 선형 분류의 한계, XOR 문제, 퍼셉트론·다층 퍼셉트론
- **MLP**: 은닉층, 활성화 함수, 순전파·역전파
- **PyTorch 기초**: 텐서, 자동 미분(Autograd), nn.Module

---

## 🧪 실습 (MLP 구현)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | PyTorch 기초 | Tensor, Autograd, nn.Module, 손실 함수, 옵티마이저 |
| 2 | 데이터 파이프라인 | TensorDataset, DataLoader, 배치 처리 |
| 3 | 학습 루프 | 순전파, 역전파, 파라미터 업데이트, train/eval 모드, Early Stopping |

**필요 패키지**: `python>=3.11`, `torch`, `numpy`, `matplotlib`

---

## 📝 과제 (간단한 Perceptron 구현)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | PyTorch 연산 | Tensor 연산, autograd, 역전파 자동화 |
| 2 | Perceptron 모델 | nn.Module로 단순 퍼셉트론 정의 |
| 3 | 학습 파이프라인 | DataLoader, optimizer, loss, 학습/검증 루프, 이진 분류 평가 |

**필요 패키지**: `python>=3.11`, `torch`, `numpy`, `matplotlib`

---

## 🎯 학습 목표

- 신경망·MLP의 기본 구조와 동작 원리 이해
- PyTorch Tensor, Autograd, nn.Module 활용
- DataLoader로 배치 단위 학습 파이프라인 구축
- 학습 루프 작성 및 Early Stopping 적용

---

## 📌 참고

- 실습·과제는 TODO 영역을 채우는 형태로 진행
- 각 노트북에 assert 기반 테스트 코드 포함
- 실습(MLP) → 과제(Perceptron) 순으로 진행 권장
