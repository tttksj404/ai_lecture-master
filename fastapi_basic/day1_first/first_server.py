from fastapi import FastAPI

app = FastAPI()

# 1. 우리서버/hello 라는 주소로 GET 요청이 들어오면 hello 함수를 실행해라
@app.get("/hello")
def hello():
    return {"message": "안녕하세요"}

# -------------------- POST 도 해보자

count = 0

# 2. /count 로 POST 요청이 오면, count 변수를 1 증가시켜라
@app.post("/count")
def increase_count():
    global count
    count += 1
    return {"message": "count 변수 증가 성공!"}


# 3. /count 로 GET 요청이 오면, 현재 count 변수를 출력해라
@app.get("/count")
def print_count():
    return {"meesage": f"현재 count = {count}"}

