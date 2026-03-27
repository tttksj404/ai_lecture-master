# FastAPI

## 학습 방향

여러분의 아이디어를 허깅페이스 모델을 통해 구현할 수 있다.
  - 텍스트로 이미지 생성
  - 이미지로 영상 생성
  - 텍스트로 추가 작업

FastAPI + HTML/CSS/JS 로 간단한 챗봇 구현
  - [주의] CORS 에러 (우선 모두 허용하는 코드로 해결)


## 서버 설정 및 실행

1. 가상환경 생성
```
python -m venv venv
```

2. 가상환경 활성화
```
source venv/Scripts/activate
```

3. fastapi, uvicorn 설치
```
pip install fastapi uvicorn
```

4. 서버 실행
```
uvicorn <파일이름>:<앱이름> --reload

uvicorn first_server:app --reload
```

5. 테스트
- GET 요청은 브라우저로 접근
- POST 요청은 curl 활용
```
curl -X POST http://127.0.0.1:8000/count
```
