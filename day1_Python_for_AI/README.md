# Day 1: AI를 위한 Python

AI 학습을 위한 Python 기초 문법 및 데이터 분석 라이브러리 입문 과정입니다.

---

## 📁 폴더 구조

```
day1_Python_for_AI/
├── 0_1_AI를_위한_Python_(Easy).ipynb   # 메인 강의 노트북
├── 단축키.ipynb                         # Jupyter 단축키 참고
├── 실습/                                # 실습 문제
│   ├── (실습-문제) 0-1_AI를 위한 Python.ipynb
│   └── (실습-힌트) 0-1_AI를 위한 Python.ipynb
└── 과제/                                # 과제
    ├── (과제-문제) 0-1_AI를 위한 Python.ipynb
    └── (과제-힌트) 0-1_AI를 위한 Python.ipynb
```

---

## 📚 주요 학습 내용

### 1. 메인 강의 (`0_1_AI를_위한_Python_(Easy).ipynb`)
- **Jupyter Lab** 사용법 및 환경 이해
- **Python 기초 문법**: 변수, if/for, 함수, 리스트
- **NumPy** 기초 및 수치 연산
- **Pandas** 기초 데이터 처리

### 2. 단축키 (`단축키.ipynb`)
- **명령 모드**: `a`(위 셀 추가), `b`(아래 셀 추가), `d d`(셀 삭제), `m`(마크다운), `y`(코드)
- **실행**: `Ctrl+Enter`, `Shift+Enter`

---

## 🧪 실습 (7단계)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 기본 자료형 | int, float, str, None, bool 및 내장 함수 |
| 2 | 컬렉션 자료형 | list, tuple, set, dict 생성 및 메서드 |
| 3 | 제어문·반복문 | if/for/while, List Comprehension, itertools |
| 4 | 함수 | 사용자 정의 함수, 람다, *args, **kwargs |
| 5 | 객체지향 | 클래스, 상속, 캡슐화, Student 예제 |
| 6 | NumPy | 배열 생성, 행렬 연산, linspace, 삼각함수 |
| 7 | Pandas | DataFrame 생성, 조회, 필터링, 집계 |

**필요 패키지**: `python>=3.11`, `numpy>=2.0.0`, `pandas>=2.0.0`, `matplotlib>=3.8.0`

---

## 📝 과제 (4단계)

| Step | 주제 | 핵심 내용 |
|------|------|-----------|
| 1 | 클래스 기초 | Dog 클래스 정의, 인스턴스 생성 |
| 2 | BankAccount | 입출금, 잔액 조회, 거래 내역 관리 |
| 3 | Pandas 기초 | DataFrame 생성, loc/iloc, 조건 필터링 |
| 4 | Pandas 심화 | groupby, pivot, melt, Tips 데이터 분석 |

**데이터셋**: Seaborn Tips (244행, 7컬럼)  
**필요 패키지**: `python>=3.11`, `pandas>=2.0.0`, `seaborn>=0.13.2`

---

## 🎯 학습 목표

- Python 기본 자료형과 제어문으로 코드 작성
- 함수와 클래스를 정의하고 활용
- NumPy로 수치 데이터 처리
- Pandas로 표 형식 데이터 조회·필터링·집계

---

## 📌 참고

- 실습·과제는 TODO 영역을 채우는 형태로 진행
- 각 노트북에 assert 기반 테스트 코드 포함
- 실습 → 과제 순으로 진행 권장
