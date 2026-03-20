# Day 3: EDA와 Scikit-learn

탐색적 데이터 분석(EDA)과 Scikit-learn을 활용한 머신러닝 파이프라인 실습 과정입니다.

---

## 📁 폴더 구조

```
day3_AI_Data_EDA/
├── 1_1_EDA와_Scikit_learn_(Easy).ipynb   # 메인 강의 노트북
├── 실습/                                   # 실습 문제
│   ├── (실습-문제) 1-1_데이터 EDA 및 모델 학습 .ipynb
│   └── (실습-힌트) 1-1_데이터 EDA 및 모델 학습.ipynb
└── 과제/                                   # 과제
    ├── (과제-문제) 1-1_데이터 EDA 및 모델 학습.ipynb
    └── (과제-힌트) 1-1_데이터 EDA 및 모델 학습.ipynb
```

---

## 📚 주요 학습 내용

### 1. 메인 강의 (`1_1_EDA와_Scikit_learn_(Easy).ipynb`)
- **EDA**: 데이터 통계 분석, 상관관계·분포 이해, 결측치·이상치 탐지
- **Scikit-learn**: 라이브러리 소개, StandardScaler 표준화, 모델 학습·평가

---

## 🧪 실습 (3단계)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | EDA | Wine 데이터 로드, 통계·상관관계·분포 시각화, 결측치·이상치(IQR) 처리 |
| 2 | 전처리·모델 학습 | Train/Test 분할, StandardScaler, LogisticRegression, 혼동행렬·Classification Report·ROC-AUC |
| 3 | 검증·시각화 | 5-fold 교차검증, PCA 2차원 축소, K-Means 군집화 시각화 |

**데이터셋**: Wine (load_wine, 178샘플, 13특성, 3클래스)  
**필요 패키지**: `python>=3.11`, `numpy>=2.0.0`, `pandas>=2.0.0`, `matplotlib>=3.8.0`, `seaborn>=0.13.2`, `scipy>=1.13.0`, `scikit-learn>=1.4.2`

---

## 📝 과제 (3단계)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 데이터 EDA | Boston Housing 로드, 기초 통계·결측치·이상치·상관관계 시각화 |
| 2 | 전처리 | Train/Test 분할, SimpleImputer, IQR 이상치 제거, StandardScaler |
| 3 | 모델 학습·평가 | 선형 회귀 학습, RMSE·MAE·R² 계산, 예측 결과 시각화 |

**데이터셋**: Boston Housing (506샘플, 13특성, 주택 가격 예측)  
**필요 패키지**: `python>=3.11`, `numpy>=2.0.0`, `pandas>=2.0.0`, `matplotlib>=3.8.0`, `seaborn>=0.13.2`, `scikit-learn>=1.4.2`

---

## 🎯 학습 목표

- EDA로 데이터 분포·상관관계·결측치·이상치 파악
- Train/Test 분할, 표준화 등 ML 전처리 파이프라인 구축
- Scikit-learn으로 분류·회귀 모델 학습 및 성능 평가
- 교차검증, PCA, K-Means 등 검증·시각화 기법 활용

---

## 📌 참고

- 실습·과제는 TODO 영역을 채우는 형태로 진행
- 각 노트북에 assert 기반 테스트 코드 포함
- 실습(분류) → 과제(회귀) 순으로 진행 권장
