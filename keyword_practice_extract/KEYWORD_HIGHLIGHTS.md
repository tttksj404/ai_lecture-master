# 키워드 직접연관 하이라이트 (힌트 전용)

- 생성 시각: 2026-04-02 22:17:37
- 범위: `keyword_practice_extract` 내부 힌트 파일 + README
- 기준: 키워드 직접 등장 문장/셀 + `# [문제였던 부분 반영]` 주석

## 데이터 생성/합성 프롬프팅
### `02_data_generation_synthetic_prompting/(과제-힌트) 2-2_합성_데이터_생성_과제.ipynb`
- cell 1: # <mark>합성데이터</mark> 생성 - 과제
- cell 1: - **<mark>프롬프팅</mark> 기법(Prompting Techniques)**: <mark>Zero-shot</mark>, <mark>Few-shot</mark>, <mark>CoT</mark>(<mark>Chain-of-Thought</mark>) 등 다양한 <mark>프롬프팅</mark> 기법의 원리와 적용 방법 이해
- cell 1: - **<mark>합성 데이터</mark> 생성(Synthetic Data Generation)**: LLM을 활용한 학습 <mark>데이터 증강</mark> 및 다양성 확보 전략
- cell 1: - <mark>Zero-shot</mark>, <mark>Few-shot</mark>, <mark>CoT</mark> 등 **다양한 <mark>프롬프팅</mark> 기법**의 차이를 이해하고, 상황에 맞게 적용할 수 있다.
- cell 1: - 페르소나(Persona) 기반 <mark>프롬프팅</mark>으로 **다양한 스타일의 데이터를 증강**할 수 있다.
- cell 1: - <mark>프롬프팅</mark> 기법에 따른 **생성 품질/다양성/일관성을 비교 분석**할 수 있다.
- cell 1: - **<mark>Zero-shot</mark> Prompting**: 예시 없이 지시문만으로 모델에게 작업을 요청하는 기법. 모델의 사전 학습된 지식에 의존
- cell 1: - **<mark>Few-shot</mark> Prompting**: 소수의 예시(1~5개)를 프롬프트에 포함하여 모델이 패턴을 학습하도록 유도하는 기법
- cell 1: - **<mark>Chain-of-Thought</mark> (<mark>CoT</mark>)**: 복잡한 추론 과제에서 단계별 사고 과정을 명시적으로 유도하여 정확도를 높이는 기법
- cell 1: - **<mark>합성 데이터</mark>(Synthetic Data)**: 실제 데이터를 기반으로 LLM을 통해 생성한 인공 데이터로, 학습 <mark>데이터 증강</mark>에 활용
- cell 1: - **<mark>Structured Output</mark> (JSON Schema)**: API 응답을 정형화된 JSON 형식으로 받아 안정적인 후처리를 가능하게 하는 기법
- cell 1: - 과제에서는 **약한 변형**으로 다양한 <mark>프롬프팅</mark> 기법(<mark>Zero-shot</mark>, <mark>Few-shot</mark>, <mark>CoT</mark>)을 비교하고, **마무리 변형**으로 LLM as a Judge를 활용한 품질 평가 파이프라인을 구축합니다.
- cell 1: - [Prompt Engineering Guide](https://www.promptingguide.ai/): 다양한 <mark>프롬프팅</mark> 기법(<mark>Zero-shot</mark>, <mark>Few-shot</mark>, <mark>CoT</mark> 등)에 대한 체계적인 설명과 예시를 제공합니다.
- cell 1: - [<mark>Chain-of-Thought</mark> Prompting (Wei et al., 2022)](https://arxiv.org/abs/2201.11903): <mark>CoT</mark> <mark>프롬프팅</mark>의 원리와 효과를 설명한 원본 논문입니다.

### `02_data_generation_synthetic_prompting/(실습-힌트) 2-2_합성_데이터_실습.ipynb`
- cell 1: # <mark>합성데이터</mark> - 실습
- cell 1: - **<mark>프롬프팅</mark> 기법과 <mark>합성 데이터</mark> 생성**: 다양한 <mark>프롬프팅</mark> 기법(<mark>Zero-shot</mark>, <mark>Few-shot</mark>, <mark>CoT</mark>)을 활용한 고품질 <mark>합성 데이터</mark> 생성
- cell 1: - **<mark>LLM as Judge</mark>를 통한 데이터 평가**: LLM 기반 자동 평가 시스템 설계 및 품질 검증
- cell 1: - <mark>Zero-shot</mark>, <mark>Few-shot</mark>, <mark>Chain-of-Thought</mark>(<mark>CoT</mark>) 등 **다양한 <mark>프롬프팅</mark> 기법의 특성을 이해**하고 목적에 맞게 선택할 수 있다.
- cell 1: - <mark>프롬프팅</mark> 기법을 활용하여 **구조화된 <mark>합성 데이터</mark>를 생성**할 수 있다.
- cell 1: - **<mark>LLM as Judge</mark> 방식**으로 생성된 데이터의 품질을 자동으로 평가하는 시스템을 설계할 수 있다.
- cell 1: - **<mark>프롬프팅</mark> 기법(Prompting Techniques)**: LLM에게 원하는 답을 이끌어내기 위한 입력 설계 방법으로, <mark>Zero-shot</mark>, <mark>Few-shot</mark>, <mark>Chain-of-Thought</mark> 등 다양한 전략 포함
- cell 1: - **<mark>Chain-of-Thought</mark>(<mark>CoT</mark>)**: 복잡한 문제를 단계별로 추론하도록 유도하여 더 정확하고 논리적인 응답을 얻는 <mark>프롬프팅</mark> 기법
- cell 1: - **<mark>합성 데이터</mark>(Synthetic Data)**: 실제 데이터가 아닌 인공적으로 생성된 데이터로, 데이터 부족 문제 해결, 개인정보 보호, 비용 절감 등에 활용
- cell 1: - **<mark>LLM as Judge</mark>**: 사람 대신 LLM을 활용하여 생성된 콘텐츠의 품질을 자동으로 평가하는 방법론
- cell 1: - **<mark>Structured Output</mark>**: LLM이 JSON 등 특정 형식을 따라 응답을 생성하도록 하는 기법으로, 후속 처리를 용이하게 함
- cell 1: - [<mark>Chain-of-Thought</mark> Prompting Paper](https://arxiv.org/abs/2201.11903): <mark>CoT</mark> <mark>프롬프팅</mark>의 원리와 효과를 다룬 원 논문으로, 왜 단계별 추론이 LLM 성능을 향상시키는지 이해할 수 있습니다.
- cell 1: - [<mark>LLM as Judge</mark> Paper](https://arxiv.org/abs/2306.05685): LLM을 평가자로 활용하는 방법론에 대한 연구로, 자동 평가 시스템 설계 시 참고할 수 있습니다.
- cell 1: - **다양한 <mark>프롬프팅</mark> 기법 비교**: <mark>Zero-shot</mark>, <mark>Few-shot</mark>, <mark>CoT</mark> <mark>프롬프팅</mark>으로 동일한 <mark>합성 데이터</mark>를 생성하고, 품질 차이를 정량적으로 비교 분석하기

### `02_data_generation_synthetic_prompting/day8_README.md`
- line 3: LLM을 활용한 소량·대량 텍스트 데이터 생성, <mark>데이터 증강</mark>, <mark>합성 데이터</mark>(Synthetic Data) 생성 및 <mark>LLM as Judge</mark> 품질 평가를 학습하는 과정입니다.
- line 26: - **대량 데이터 생성**: 소형 모델로 생성, <mark>LLM as Judge</mark>로 필터링
- line 27: - **<mark>데이터 증강</mark> vs <mark>합성 데이터</mark>**: 개념 이해
- line 28: - **이미지 <mark>데이터 증강</mark>**: 기초 개념
- line 32: ## 🧪 실습 (<mark>합성 데이터</mark> 생성·평가)
- line 37: | 2 | <mark>프롬프팅</mark> 기법 비교 | <mark>Zero-shot</mark>, <mark>Few-shot</mark>, <mark>Chain-of-Thought</mark>(<mark>CoT</mark>) |
- line 38: | 3 | 구조화된 <mark>합성 데이터</mark> | JSON 형식 지정, <mark>Structured Output</mark>, temperature |
- line 39: | 4 | <mark>LLM as Judge</mark> | 품질 자동 평가, 평가 기준, 필터링 |
- line 45: ## 📝 과제 (<mark>합성 데이터</mark> 생성 심화)
- line 49: | 1 | <mark>프롬프팅</mark> 기법 비교 | <mark>Zero-shot</mark>, <mark>Few-shot</mark>, <mark>CoT</mark>로 번역 품질 비교 |

### `INDEX.md`
- line 7: ## 2) 데이터 생성/합성 <mark>프롬프팅</mark>

## EDA와 선형회귀
### `01_eda_linear_regression/(과제-힌트) 0-2_로지스틱 회귀 구현.ipynb`
- cell 1: # <mark>로지스틱 회귀</mark> 구현 - 과제
- cell 1: - **분류 모델 구현**: <mark>로지스틱 회귀</mark>를 통한 이진 분류 모델 구현
- cell 1: - **<mark>경사 하강법</mark> 적용**: 미니배치 <mark>경사 하강법</mark>을 활용한 모델 학습 및 최적화
- cell 1: - <mark>로지스틱 회귀</mark>의 핵심 개념과 흐름을 이해하고, NumPy로 **직접 구현**하여 이진 분류 모델을 **학습·평가**할 수 있다.
- cell 1: - BCE 손실 함수의 **그래디언트를 계산**하고 <mark>경사 하강법</mark>으로 파라미터를 **업데이트**할 수 있다.
- cell 1: - 미니배치 <mark>경사 하강법</mark>을 적용하여 모델을 **학습**시키고, **손실 곡선과 정확도**를 통해 수렴 과정을 **해석**할 수 있다.
- cell 1: - **<mark>경사 하강법</mark>(Gradient Descent)**: 그래디언트를 이용해 손실을 줄이는 방향으로 파라미터를 반복적으로 업데이트하는 최적화 알고리즘이다.
- cell 1: - <mark>선형 회귀</mark>의 기본 개념(가설 함수, 손실 함수, <mark>경사 하강법</mark>)
- cell 1: - 실습에서 다뤘던 **<mark>선형 회귀</mark>의 <mark>경사 하강법</mark>**을 출발점으로 사용합니다.
- cell 1: - [Logistic Regression From Scratch in Python NumPy](https://towardsdatascience.com/logistic-regression-from-scratch-in-python-ec66603592e2): 벡터 연산만으로 <mark>로지스틱 회귀</mark>를 구현하는 과정을 단계별로 설명합니다.
- cell 2: - **Step 2 (40분)**: <mark>로지스틱 회귀</mark> 모델 학습 — 시그모이드 함수, BCE 손실, 그래디언트 계산 및 파라미터 업데이트 구현
- cell 2: - **사용 목적**: 이진 분류 <mark>로지스틱 회귀</mark> 모델 학습 및 평가
- cell 2: - **문제 개요**: 이 과제는 **<mark>로지스틱 회귀</mark>를 이용한 이진 분류**의 기초를 다지기 위해 설계되었습니다. 학습자는 **시그모이드 함수, BCE 손실, <mark>경사 하강법</mark>, 미니배치 학습**을 코드로 확인하고, 최종적으로 **모델을 학습·평가·최적화·해석**할 수 있어야 합니다.
- cell 2: - **Step 2 — <mark>로지스틱 회귀</mark> 모델 학습**

### `01_eda_linear_regression/(과제-힌트) 1-1_데이터 EDA 및 모델 학습.ipynb`
- cell 1: # 데이터 <mark>EDA</mark> 및 모델 학습 - 과제
- cell 1: - **탐색적 데이터 분석(Exploratory Data Analysis, <mark>EDA</mark>)**: 데이터의 구조와 특성을 이해하고 시각화를 통해 인사이트 도출
- cell 1: - **머신러닝 모델 학습 및 평가**: <mark>선형 회귀</mark> 모델을 활용한 지도 학습 파이프라인 구현
- cell 1: - `SimpleImputer`, `<mark>StandardScaler</mark>` 등을 사용해 **데이터 전처리 파이프라인**을 구축하고 train/test split을 수행할 수 있다.
- cell 1: - 머신러닝의 기본 흐름(학습-예측-평가)을 이해하고, **<mark>선형 회귀</mark> 모델을 학습**시킬 수 있다.
- cell 1: - **탐색적 데이터 분석(Exploratory Data Analysis, <mark>EDA</mark>)**: 데이터의 분포, 결측치, 이상치, 변수 간 관계를 시각화하고 분석하여 데이터 특성을 파악하는 과정
- cell 1: - **<mark>선형 회귀</mark>(<mark>Linear Regression</mark>)**: 입력 변수와 출력 변수 간의 선형 관계를 모델링하여 연속형 값을 예측하는 지도 학습 알고리즘
- cell 1: - (선택) <mark>선형 회귀</mark>의 수학적 원리 (없어도 실습 가능하도록 설명 제공)
- cell 1: - 실습에서 다뤘던 **NumPy 기반 <mark>선형 회귀</mark> 구현**을 출발점으로 사용합니다.
- cell 1: - [Comprehensive Guide to <mark>EDA</mark> with Python](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15): pandas와 seaborn을 활용한 다양한 <mark>EDA</mark> 기법과 시각화 방법을 단계별로 설명합니다. 데이터 탐색 과정에서 어떤 질문을 던지고, 어떻게 인사이트를 도출하는지 배울 수 있습니다.
- cell 1: - [Understanding Regression Metrics (RMSE, MAE, R²)](https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234): <mark>회귀 모델</mark>의 성능 지표들이 각각 무엇을 의미하는지, 어떤 상황에서 어떤 지표를 사용해야 하는지에 대한 실용적 가이드입니다.
- cell 1: - **다양한 <mark>회귀 모델</mark> 비교**: Ridge, Lasso, ElasticNet 등 정규화가 적용된 선형 모델과 Decision Tree, Random Forest 등 비선형 모델을 학습시켜 성능을 비교하고, 각 모델의 장단점을 분석하기
- cell 2: - **Step 1**: 데이터 로딩 및 <mark>EDA</mark> - 보스턴 주택 가격 데이터를 로드하고, 기초 통계, 결측치, 이상치, 상관관계를 탐색하며 데이터 특성 파악
- cell 2: - **Step 2**: 데이터 전처리 워크플로우 - train/test split, 결측치 처리(SimpleImputer), 이상치 제거(IQR), 표준화(<mark>StandardScaler</mark>) 수행

### `01_eda_linear_regression/(실습-힌트) 0-2_NumPy를 이용한 선형 회귀 모델 구현.ipynb`
- cell 1: # NumPy를 이용한 <mark>선형 회귀</mark> 모델 구현 - 실습
- cell 1: - <mark>선형 회귀</mark> 모델 학습
- cell 1: - <mark>경사 하강법</mark> 기반 최적화
- cell 1: - `np.linalg.lstsq`와 SVD를 활용해 <mark>선형 회귀</mark>의 최적 파라미터를 구할 수 있다.
- cell 1: - <mark>경사 하강법</mark>으로 모델을 학습하고 MSE 손실을 계산할 수 있다.
- cell 1: - **<mark>경사 하강법</mark>(Gradient Descent)**: 손실 함수의 기울기를 따라 파라미터를 반복적으로 업데이트하여 최적값을 찾는 알고리즘
- cell 2: - **Step 3**: <mark>경사 하강법</mark> 학습 - 손실 함수(MSE) 계산, 그래디언트 업데이트, 학습 곡선 시각화
- cell 2: - **사용 목적**: 연속형 변수를 이용한 <mark>선형 회귀</mark> 모델 학습 및 예측 성능 평가
- cell 2: - **문제 개요**: 이 실습은 **NumPy를 활용한 <mark>선형 회귀</mark> 모델의 직접 구현**을 통해 머신러닝의 기초 원리를 익히기 위해 설계되었습니다. 학습자는 **데이터 정규화, 선형대수 기반 최적해 계산, <mark>경사 하강법</mark>**을 코드로 확인하고, 최종적으로 **모델을 학습하고 평가하며 학습 과정을 시각화**할 수 있어야 합니다.
- cell 2: - **반복적 최적화**: <mark>경사 하강법</mark>을 구현하여 손실을 최소화
- cell 2: - **TODO 4:** NumPy의 **`np.linalg.lstsq` 함수를 활용**하여 <mark>선형 회귀</mark> 파라미터 구하기 (*연결 핵심개념: 최소제곱법, 특이값 분해(SVD)*)
- cell 2: - **Step 3 — <mark>경사 하강법</mark>과 손실 계산**
- cell 2: - **TODO 6:** 반복문을 통해 파라미터를 업데이트하는 **<mark>경사 하강법</mark>(Gradient Descent) 알고리즘 구현**하기(*연결 핵심개념: <mark>경사 하강법</mark> 구현, 손실 함수 계산*)
- cell 3: <mark>선형 회귀</mark>에서는 주로 **MSE(Mean Squared Error, 평균 제곱 오차)** 를 손실 함수로 사용합니다:

### `01_eda_linear_regression/(실습-힌트) 1-1_데이터 EDA 및 모델 학습.ipynb`
- cell 1: # 데이터 <mark>EDA</mark> 및 모델 학습 - 실습
- cell 1: - **탐색적 데이터 분석(<mark>EDA</mark>)**: 데이터 분포, 상관관계, 결측치·이상치 탐색 및 시각화
- cell 1: - **지도학습 분류 모델**: 데이터 전처리, <mark>로지스틱 회귀</mark> 학습, 성능 평가 및 교차검증
- cell 1: - scikit-learn의 train_test_split 및 <mark>StandardScaler</mark>로 데이터를 **분할·정규화**할 수 있다.
- cell 1: - **<mark>EDA</mark>(탐색적 데이터 분석)**: 데이터 분포, 중앙값·사분위수·상관관계 등을 시각화를 통해 탐색하는 기법
- cell 1: - **<mark>StandardScaler</mark>**: 피처별 평균을 0, 분산을 1로 표준화하여 머신러닝 모델 학습을 안정화하는 전처리 기법
- cell 2: - **Step 1**: 데이터 로딩 및 탐색적 데이터 분석(<mark>EDA</mark>) - Wine 데이터셋 로드, 통계량 계산, 상관관계·분포 시각화, 결측치·이상치 탐지 및 처리
- cell 2: - **Step 2**: 머신러닝 전처리 및 모델 학습 - Train/Test 분할, <mark>StandardScaler</mark> 적용, Logistic Regression 학습 및 성능 평가
- cell 2: - **문제 개요**: 이 실습은 머신러닝의 기초 개념을 이해하고 실무에서 사용하는 ML 파이프라인 전체 흐름을 경험하기 위해 설계되었습니다. 학습자는 **<mark>EDA</mark>, 데이터 전처리, 모델 학습, 성능 평가**를 코드로 확인하고, 최종적으로 **데이터로부터 인사이트를 도출하고 분류 모델을 학습·평가**할 수 있어야 합니다.
- cell 2: - **Step 1**: Wine 데이터셋 로드 및 <mark>EDA</mark> 수행
- cell 2: - **Step 2**: 데이터 전처리 및 <mark>로지스틱 회귀</mark> 모델 학습
- cell 2: - **TODO 7**: train/test 분할 및 <mark>StandardScaler</mark> 표준화 적용하기
- cell 7: ## Step 1: 데이터 로딩 및 탐색적 데이터 분석(<mark>EDA</mark>)
- cell 7: **<mark>EDA</mark> (탐색적 데이터 분석)란?**

### `01_eda_linear_regression/day2_README.md`
- line 1: # Day 2: AI를 위한 Math (선형·<mark>로지스틱 회귀</mark>)
- line 3: 머신러닝 기초 개념과 <mark>선형 회귀</mark>·<mark>로지스틱 회귀</mark>를 NumPy로 직접 구현하는 과정입니다.
- line 11: ├── 0_2_<mark>선형회귀</mark>와_<mark>로지스틱회귀</mark>_(Easy).ipynb   # 메인 강의 노트북
- line 13: │   ├── (실습-문제) 0-2_NumPy를 이용한 <mark>선형 회귀</mark> 모델 구현.ipynb
- line 14: │   └── (실습-힌트) 0-2_NumPy를 이용한 <mark>선형 회귀</mark> 모델 구현.ipynb
- line 16: ├── (과제-문제) 0-2_<mark>로지스틱 회귀</mark> 구현.ipynb
- line 17: └── (과제-힌트) 0-2_<mark>로지스틱 회귀</mark> 구현.ipynb
- line 24: ### 1. 메인 강의 (`0_2_<mark>선형회귀</mark>와_<mark>로지스틱회귀</mark>_(Easy).ipynb`)
- line 26: - **<mark>선형 회귀</mark>**: 추세선, <mark>회귀 모델</mark>의 기본
- line 27: - **<mark>로지스틱 회귀</mark>**: 분류 문제와 확률 예측

### `01_eda_linear_regression/day3_README.md`
- line 3: 탐색적 데이터 분석(<mark>EDA</mark>)과 Scikit-learn을 활용한 머신러닝 파이프라인 실습 과정입니다.
- line 13: │   ├── (실습-문제) 1-1_데이터 <mark>EDA</mark> 및 모델 학습 .ipynb
- line 14: │   └── (실습-힌트) 1-1_데이터 <mark>EDA</mark> 및 모델 학습.ipynb
- line 16: ├── (과제-문제) 1-1_데이터 <mark>EDA</mark> 및 모델 학습.ipynb
- line 17: └── (과제-힌트) 1-1_데이터 <mark>EDA</mark> 및 모델 학습.ipynb
- line 25: - **<mark>EDA</mark>**: 데이터 통계 분석, 상관관계·분포 이해, 결측치·이상치 탐지
- line 26: - **Scikit-learn**: 라이브러리 소개, <mark>StandardScaler</mark> 표준화, 모델 학습·평가
- line 34: | 1 | <mark>EDA</mark> | Wine 데이터 로드, 통계·상관관계·분포 시각화, 결측치·이상치(IQR) 처리 |
- line 35: | 2 | 전처리·모델 학습 | Train/Test 분할, <mark>StandardScaler</mark>, LogisticRegression, 혼동행렬·Classification Report·ROC-AUC |
- line 47: | 1 | 데이터 <mark>EDA</mark> | Boston Housing 로드, 기초 통계·결측치·이상치·상관관계 시각화 |

### `INDEX.md`
- line 3: ## 1) EDA와 <mark>선형회귀</mark>

## RAG 구현 & LangGraph
### `03_rag_langgraph/(과제-힌트) 4-1_RAG_기반_Customer_Service_AI_에이전트_개발.ipynb`
- cell 1: # <mark>RAG</mark> 기반 Customer Service AI 에이전트 개발 - 과제
- cell 1: - **<mark>Retriever</mark> 설정 최적화**: top_k 등 검색 파라미터 조정에 따른 <mark>RAG</mark> 응답 품질 변화 분석
- cell 1: - **<mark>RAG</mark> 파이프라인 응용**: 실습에서 구현한 파이프라인을 기반으로 설정을 최적화하고 근거를 제시
- cell 1: - top_k 값을 변경했을 때 <mark>RAG</mark> 응답 품질이 어떻게 달라지는지 비교하고 차이점을 설명할 수 있다
- cell 1: - Yes24 고객 서비스 시나리오에 적합한 <mark>RAG</mark> 설정(chunk_size, overlap, top_k)을 선택하고 논리적 근거를 제시할 수 있다
- cell 1: - **<mark>Retriever</mark> 파라미터**: top_k(반환 문서 수) 등 검색 설정이 <mark>RAG</mark> 응답 품질에 미치는 영향. 적은 k는 정보 누락 위험, 많은 k는 관련 없는 정보 포함 위험
- cell 1: - **4-1 실습 완료 필수**: <mark>RAG</mark> 파이프라인(<mark>임베딩</mark>, Vector Store, <mark>Retriever</mark>, <mark>LangGraph</mark>) 구현 경험
- cell 1: - 이 과제는 **4-1 실습에서 구현한 <mark>RAG</mark> 파이프라인을 기반**으로 합니다.
- cell 1: - [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401): <mark>RAG</mark> 원본 논문 (Lewis et al., 2020). RAG의 이론적 배경과 효과 이해
- cell 1: - [LangChain <mark>Retriever</mark> 공식 문서](https://python.langchain.com/docs/modules/data_connection/<mark>retriever</mark>s/): <mark>Retriever</mark> 설정 옵션 및 고급 기능
- cell 2: - `<mark>langgraph</mark>>=0.2.0`
- cell 2: - **Step 3 (15분)**: <mark>Retriever</mark> 설정 변경 및 비교 — top_k 등 변경 → 검색 품질 비교
- cell 2: - **문제 개요**: 이 과제는 **<mark>RAG</mark> 파이프라인의 구성 요소를 판단하고 선택하는 역량**을 평가합니다. 학습자는 **청킹 전략, <mark>Retriever</mark> 설정 등을 변경**하며 결과를 비교하고, 최종적으로 **선택한 구성에 대한 논리적 근거를 제시**할 수 있어야 합니다.
- cell 2: - **<mark>Retriever</mark> 설정 비교**: top_k 변경에 따른 <mark>RAG</mark> 응답 품질 비교

### `03_rag_langgraph/(과제-힌트) 4-2(1)_ReAct_기반_Agent_서비스_개발.ipynb`
- cell 1: - **CoT <mark>StateGraph</mark> 구현**: 명시적 추론 단계가 포함된 Agent 워크플로우 구현
- cell 1: - CoT 패턴 <mark>StateGraph</mark>를 구현할 수 있다
- cell 1: - **CoT <mark>StateGraph</mark>**: 도구 호출 전에 명시적 추론 단계(Reasoning)를 추가하여 Agent가 체계적으로 문제를 분석하고 계획을 수립하도록 하는 패턴.
- cell 1: - Chapter 4-1 <mark>RAG</mark> 실습 경험: Vector Store 구축, <mark>Retriever</mark> 활용
- cell 1: - [<mark>LangGraph</mark> 공식 문서](https://langchain-ai.github.io/<mark>langgraph</mark>/): 상태 그래프 기반 Agent 워크플로우 가이드
- cell 2: - `<mark>langgraph</mark>>=0.2.0`
- cell 2: - Python 3.10 이상 권장 (<mark>LangGraph</mark>의 타입 힌팅 기능 활용)
- cell 2: - **Step 3 (15분)**: CoT <mark>StateGraph</mark> 구현 — 명시적 추론 단계가 포함된 Agent 워크플로우 구현
- cell 2: - **문제 개요**: 이 과제는 **Agent 구조의 재활용과 <mark>StateGraph</mark> 확장 역량**을 평가합니다. 학습자는 실습에서 구현한 쿠폰 발급 도구를 **환불 처리 도구로 변형**하고, **CoT 패턴 <mark>StateGraph</mark>**를 구현할 수 있어야 합니다.
- cell 2: - CoT 패턴 <mark>StateGraph</mark> 구현
- cell 2: - **Step 3 — CoT <mark>StateGraph</mark> 구현**
- cell 2: - **TODO 3**: CoT 패턴 <mark>StateGraph</mark> 구현 *(연결: <mark>LangGraph</mark> / 학습목표3)*
- cell 2: - **1줄 요약**: 명시적 추론 단계가 포함된 CoT 패턴 <mark>StateGraph</mark> 구현
- cell 3: %pip install langchain langchain-openai langchain-upstage <mark>langgraph</mark> langchain-community langchain-text-splitters chromadb tiktoken python-dotenv -q

### `03_rag_langgraph/(과제-힌트) 4-2(2)_Multi-Agent_대표_패턴_학습.ipynb`
- cell 1: - <mark>LangGraph</mark> <mark>StateGraph</mark>를 사용하여 다중 Worker 워크플로우를 구성할 수 있다
- cell 1: - **<mark>StateGraph</mark> 확장**: 여러 노드를 연결하고 상태를 공유하는 <mark>LangGraph</mark> 워크플로우 구성 방법. 다중 Worker 구조에서는 State 필드를 Worker별로 구분하여 관리한다.
- cell 1: - <mark>LangGraph</mark> <mark>StateGraph</mark> 사용법, 노드 함수 정의 방법
- cell 1: - [<mark>LangGraph</mark> Multi-Agent 가이드](https://python.langchain.com/docs/<mark>langgraph</mark>): Multi-Agent 구현 심화
- cell 1: - [<mark>LangGraph</mark> Supervisor 예제](https://langchain-ai.github.io/<mark>langgraph</mark>/tutorials/multi_agent/agent_supervisor/): Supervisor 패턴 공식 튜토리얼
- cell 1: - <mark>LangGraph</mark> 조건부 엣지(conditional_edge) 사용하여 동적 Worker 선택 구현
- cell 2: | `<mark>langgraph</mark>` | ≥0.2.0 | Multi-Agent 워크플로우 |
- cell 2: - TODO 5: <mark>LangGraph</mark> 워크플로우 구성 (Fan-out/Fan-in)
- cell 4: %pip install "langchain>=0.3.0" "langchain-openai>=0.2.0" "langchain-upstage>=0.3.0" "<mark>langgraph</mark>>=0.2.0" "python-dotenv>=1.0.0" -q
- cell 8: - <mark>LangGraph</mark> <mark>StateGraph</mark>: 상태 기반 워크플로우 정의
- cell 12: - **예상 결과**: TypedDict 클래스가 정의되어 <mark>StateGraph</mark>에서 사용 가능
- cell 13: # [<mark>문제였던 부분 반영</mark>]
- cell 13: # 스켈레톤: 기본 Agent 클래스 + <mark>LangGraph</mark> State
- cell 13: # <mark>LangGraph</mark> State 정의 (병렬 실행을 위한 Annotated reducer 사용)

### `03_rag_langgraph/(실습-힌트) 4-1_RAG_기반_Customer_Service_AI_에이전트_개발.ipynb`
- cell 1: # <mark>RAG</mark> 기반 Customer Service AI 에이전트 개발
- cell 1: - **<mark>RAG</mark> 파이프라인 구축**: 문서 로딩 → 청킹 → <mark>임베딩</mark> → Vector Store 저장 → 검색 → LLM 답변 생성까지의 전체 흐름
- cell 1: - 텍스트 <mark>임베딩</mark>의 원리(코사인 유사도)를 이해하고 Vector Store에 문서를 저장할 수 있다
- cell 1: - <mark>LangGraph</mark> <mark>StateGraph</mark>를 사용하여 <mark>검색-생성</mark> <mark>RAG</mark> 파이프라인을 구현하고 실행할 수 있다
- cell 1: - **<mark>RAG</mark>(Retrieval-Augmented Generation)**: LLM의 환각/지식 한계를 외부 문서 검색으로 보완하는 기법. 질문 → 관련 문서 검색 → 검색 결과를 컨텍스트로 포함하여 LLM에 전달 → 정확한 답변 생성의 흐름으로 동작
- cell 1: - **<mark>임베딩</mark>(Embedding)**: 텍스트를 고차원 벡터 공간(예: 1536차원)에 표현하는 기술. 의미가 유사한 텍스트는 벡터 공간에서 가까운 위치에 배치되어 코사인 유사도로 유사성 측정 가능
- cell 1: - **Vector Store**: <mark>임베딩</mark> 벡터를 저장하고 유사도 기반 검색(Approximate Nearest Neighbor)을 수행하는 특수 데이터베이스. ChromaDB, FAISS, Pinecone 등이 대표적
- cell 1: - **<mark>Retriever</mark>**: 사용자 쿼리를 <mark>임베딩</mark>하고 Vector Store에서 유사도가 높은 문서(top-k)를 검색하여 반환하는 컴포넌트. LangChain에서 `vectorstore.as_<mark>retriever</mark>()`로 생성
- cell 2: - `<mark>langgraph</mark>>=0.2.0`
- cell 2: - **Step 7 (10분)**: 전체 <mark>RAG</mark> 파이프라인 (<mark>LangGraph</mark>) — Step 2와 비교하여 <mark>RAG</mark> 효과 확인
- cell 2: - **문제 개요**: 이 실습은 **"LLM만으로는 왜 안 되는가?"**라는 질문에서 시작합니다. 학습자는 LLM의 한계(환각, 도메인 지식 부재)를 직접 확인하고, **키워드 검색 → 의미 기반 검색 → 청킹 전략**으로 단계별 해결책을 발견하며, 최종적으로 **<mark>LangGraph</mark> <mark>StateGraph</mark>를 활용한 <mark>RAG</mark> 파이프라인**으로 정확한 고객 서비스 답변을 생성할 수 있어야 합니다.
- cell 2: - **Vector Store 활용**: 문서 <mark>임베딩</mark> 및 ChromaDB 저장/검색
- cell 2: - **<mark>RAG</mark> 파이프라인 구현**: <mark>LangGraph</mark> <mark>StateGraph</mark>로 <mark>retrieve → generate</mark> 워크플로우 구현
- cell 2: - **사용 목적**: <mark>RAG</mark> 파이프라인 구축을 위한 검색 대상 문서

### `03_rag_langgraph/(실습-힌트) 4-2(1)_ReAct_기반_Agent_서비스_개발.ipynb`
- cell 1: - <mark>LangGraph</mark>를 활용하여 상태 그래프 기반 Agent 워크플로우를 정의하고 제어할 수 있다
- cell 1: - **<mark>RAG</mark> (Retrieval-Augmented Generation)**: 외부 지식 베이스에서 관련 문서를 검색(Retrieve)하여 LLM의 컨텍스트에 추가함으로써 정확도와 신뢰성을 높이는 기법.
- cell 1: - **<mark>LangGraph</mark>**: LangChain 생태계의 확장 라이브러리로, 상태 그래프(State Graph)를 사용하여 Agent의 워크플로우를 명시적으로 정의하고, 조건부 분기와 반복을 제어할 수 있다.
- cell 1: - Chapter 4-1 <mark>RAG</mark> 실습 경험: Vector Store 구축, <mark>Retriever</mark> 활용, 문서 검색 파이프라인 구현
- cell 2: - `<mark>langgraph</mark>>=0.2.0`
- cell 2: - **Step 3 (8분)**: +Tool — 행동 가능하게 만들기, <mark>RAG</mark> 정책 검색 도구 구현
- cell 2: - **Step 6 (4분)**: <mark>StateGraph</mark> 소개 — Graph 구현 도구 이해
- cell 2: - <mark>RAG</mark> 기반 정책 검색 도구 구현
- cell 2: - <mark>StateGraph</mark>로 Direct/ReAct 패턴 구현
- cell 2: - **TODO 1**: <mark>RAG</mark> 정책 검색 도구 구현 *(연결: Tool-use / 학습목표1)*
- cell 2: - **1줄 요약**: <mark>retriever</mark>를 사용하여 정책 문서를 검색하고 결과를 문자열로 반환
- cell 2: - **TODO 2**: Direct 패턴 <mark>StateGraph</mark> 구현 *(연결: <mark>LangGraph</mark> / 학습목표3)*
- cell 2: - **1줄 요약**: 도구 1회 실행 후 종료되는 Direct 패턴 <mark>StateGraph</mark> 구현
- cell 5: %pip install "langchain>=0.3.0" "langchain-openai>=0.2.0" "langchain-upstage>=0.3.0" "<mark>langgraph</mark>>=0.2.0" "langchain-community>=0.3.0" "langchain-text-splitters>=0.3.0" "chromadb>=0.5.0" "tiktoken>=0.7.0" "python-dotenv>=1.0.0" -q

### `03_rag_langgraph/(실습-힌트) 4-2(2)_Multi-Agent_대표_패턴_학습.ipynb`
- cell 1: - **<mark>LangGraph</mark> 워크플로우 구성**: <mark>StateGraph</mark>를 활용한 에이전트 간 상태 공유 및 흐름 제어
- cell 1: - <mark>LangGraph</mark> <mark>StateGraph</mark>를 사용하여 Agent 간 상태 공유 워크플로우를 구성할 수 있다
- cell 1: - **<mark>StateGraph</mark>**: <mark>LangGraph</mark>에서 제공하는 상태 기반 워크플로우 정의 클래스. 노드(Agent)와 엣지(흐름)로 구성되며, State 객체를 통해 Agent 간 정보를 전달한다. TypedDict를 상속하여 State 스키마를 정의한다.
- cell 2: - `<mark>langgraph</mark>>=0.2.0`: Multi-Agent 워크플로우
- cell 2: - Python 3.10 이상 권장 (<mark>LangGraph</mark>의 타입 힌팅 기능 활용)
- cell 2: - **문제 개요**: 이 실습은 Multi-Agent 시스템의 필요성을 이해하고, Planner-Worker 및 Reflection 패턴을 구현하기 위해 설계되었습니다. 학습자는 <mark>LangGraph</mark> <mark>StateGraph</mark>를 사용하여 에이전트 간 상태 공유 워크플로우를 구성하고, 최종적으로 Multi-Agent 대표 패턴 5가지의 특징과 적합한 상황을 비교 설명할 수 있어야 합니다.
- cell 4: %pip install "langchain>=0.3.0" "langchain-openai>=0.2.0" "langchain-upstage>=0.3.0" "<mark>langgraph</mark>>=0.2.0" "python-dotenv>=1.0.0" -q
- cell 10: # [<mark>문제였던 부분 반영</mark>]
- cell 12: #### <mark>LangGraph</mark>란?
- cell 12: **<mark>LangGraph</mark>**는 LangChain 팀이 개발한 워크플로우 오케스트레이션 라이브러리입니다:
- cell 12: - **<mark>StateGraph</mark>**: 상태 기반 그래프로 에이전트 흐름 정의. `TypedDict`를 상속하여 State 스키마 정의
- cell 12: #### <mark>LangGraph</mark> State 흐름도
- cell 12: │                     <mark>LangGraph</mark> State 흐름                          │
- cell 13: ### Guided Build: <mark>LangGraph</mark> State 및 기본 구조

### `03_rag_langgraph/day10_README.md`
- line 1: # Day 10: LangChain과 <mark>RAG</mark>
- line 3: LangChain 기반으로 <mark>RAG</mark>(Retrieval-Augmented Generation) 파이프라인을 구성하고, 검색 기반 고객지원 AI 에이전트를 구현하는 과정입니다.
- line 25: - **<mark>RAG</mark> 개념**: LLM 생성에 외부 지식 검색 결과를 결합
- line 26: - **LangChain 구성 요소**: 문서 로딩, 분할, <mark>임베딩</mark>, <mark>벡터스토어</mark>, 리트리버, 체인
- line 32: ## 🧪 실습 (<mark>RAG</mark> 기반 고객지원 에이전트)
- line 37: | 2 | Chunking·<mark>임베딩</mark> | 문서 분할 전략, <mark>임베딩</mark> 생성 |
- line 38: | 3 | 벡터 검색 | <mark>벡터스토어</mark> 구축, 유사도 검색, top-k 실험 |
- line 39: | 4 | <mark>RAG</mark> 체인 구성 | <mark>Retriever</mark> + LLM 결합, 프롬프트 템플릿 적용 |
- line 46: ## 📝 과제 (<mark>RAG</mark> 에이전트 심화)
- line 62: - <mark>RAG</mark> 파이프라인(문서→<mark>임베딩</mark>→<mark>검색→생성</mark>) 전체 흐름 설명

### `03_rag_langgraph/day11_README.md`
- line 3: LangChain 기반으로 Multi-turn 대화 흐름을 구성하고, ReAct 에이전트와 Multi-Agent 대표 패턴을 학습하며, Gradio로 나만의 <mark>RAG</mark> 시스템을 서비스 형태로 구현하는 과정입니다.
- line 37: - **<mark>RAG</mark> 서비스화**: <mark>검색-생성</mark> 파이프라인을 사용자 앱으로 연결
- line 66: **필요 패키지**: `python>=3.11`, `langchain`, `<mark>langgraph</mark>`(선택), `gradio`, `openai`(또는 호환 API), `python-dotenv`

### `INDEX.md`
- line 10: ## 3) <mark>RAG</mark> 구현 & <mark>LangGraph</mark>
