# Day10 RAG 완전 정리 (노션 업로드용)

이 문서는 Day10 수업 내용을 기반으로, **노션 페이지에 그대로 붙여넣을 수 있게** 정리한 상세 가이드입니다.
목표는 아래 4가지입니다.

1. LLM 단독 한계를 정확히 이해한다.
2. Tool/Agent/RAG 차이를 명확히 구분한다.
3. LangChain으로 RAG 파이프라인을 직접 구현한다.
4. LangGraph + LangSmith로 운영 가능한 구조로 확장한다.

---

## 0. 한 줄 요약

- **LLM 단독**: 똑똑하지만 최신/사내 데이터를 모르면 틀릴 수 있다.
- **Tool/Agent**: LLM이 못하는 기능(검색, 계산, DB조회)을 외부 함수로 호출한다.
- **RAG**: 외부 문서를 검색해서 프롬프트에 함께 넣고 답하게 만든다.
- **LangChain**: 이 전체 흐름(입력 → 가공 → 호출 → 후처리)을 파이프라인 코드로 연결한다.
- **LangGraph**: 분기/반복/상태유지까지 가능한 워크플로우 엔진이다.
- **LangSmith**: 디버깅, 추적(Tracing), 평가(Eval) 도구다.

---

## 1. 왜 RAG가 필요한가

## 1-1. LLM을 Python으로 직접 개발할 때의 대표 단점

1. 최신 정보를 모른다.
2. 사내 DB, 파일, 실시간 데이터에 기본적으로 접근하지 못한다.
3. 뉴스/정책/가격 등 시간 민감 정보를 틀리게 답할 수 있다.
4. 모델 성능이 낮으면 답변 품질 자체가 낮다.
5. 계산/규칙 기반 업무를 안정적으로 처리하기 어렵다.

즉, LLM 하나만으로는 실무 요구를 만족시키기 어렵다.

## 1-2. 해결 방향

1. LLM이 못하는 것을 Python 함수로 만든다.
2. LLM이 필요할 때 그 함수를 호출하게 한다.
3. 외부 정보를 검색해 컨텍스트로 넣고 답하게 한다.

이 구조가 바로 **Tool/Agent + RAG** 조합이다.

---

## 2. Tool / Agent / RAG 개념 정리

## 2-1. Tool

- Tool은 함수다.
- 예: 웹 검색, DB 조회, 계산기, 환율 API, 재고 조회.
- LLM이 자연어로 직접 못하는 일을 안전하게 위임한다.

## 2-2. Agent

- Agent는 "언제 어떤 Tool을 쓸지" 스스로 판단하는 실행자다.
- 핵심은 **자체 판단 + 순차 실행 + 결과 통합**이다.

## 2-3. RAG

- Retrieval Augmented Generation.
- 검색(Retrieval)으로 관련 문서를 찾고,
- 생성(Generation)에서 그 문서를 근거로 답한다.
- 목표: 환각 감소, 도메인 정확도 향상, 최신성 보강.

---

## 3. LLM 서비스/프레임워크 선택지

| 구분 | 도구 | 특징 |
|---|---|---|
| 노코드 | n8n | 빠른 자동화, 시각적 구성 |
| 중간 코드 | crewAI, LiteLLM | 비교적 빠른 구성, 일부 추상화 |
| 완전 코드 | LangChain, LangGraph | 세밀 제어, 복잡 워크플로우 구현 |

실무에서 복잡도가 올라갈수록 **LangChain + LangGraph + LangSmith** 조합이 유리하다.

---

## 4. LangChain 핵심 개념

LangChain은 LLM 호출 라이브러리가 아니라, **LLM 앱 파이프라인 프레임워크**다.

기본 흐름:

1. 입력 받기
2. 프롬프트 가공
3. 모델 호출
4. 출력 파싱
5. 다음 단계로 연결

LCEL 파이프 (`|`)로 각 단계를 선언형으로 연결한다.

---

## 5. 실습 환경 세팅

## 5-1. 패키지 설치

```bash
pip install -U \
  python-dotenv \
  langchain langchain-core langchain-community \
  langchain-openai langchain-huggingface \
  langgraph langsmith \
  chromadb faiss-cpu \
  pypdf
```

## 5-2. `.env` 예시

```env
UPSTAGE_API_KEY=YOUR_UPSTAGE_API_KEY
LANGCHAIN_API_KEY=YOUR_LANGSMITH_KEY
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=day10-rag
```

---

## 6. LangChain 기초 코드 (직선형 체인)

아래는 사용자 질문 1개를 받아 답하는 가장 기본적인 체인이다.

```python
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv("UPSTAGE_API_KEY")

model = ChatOpenAI(
    model="solar-pro",
    base_url="https://api.upstage.ai/v1/solar",
    api_key=api_key,
    temperature=0,
)

prompt = ChatPromptTemplate.from_template(
    "다음 질문에 친절하고 정확하게 답해줘. 질문: {question}"
)

chain = prompt | model | StrOutputParser()

query = "치킨은 왜 맛있어?"
result = chain.invoke({"question": query})

print(result)
```

---

## 7. Tool 바인딩 예제 (수동 루프)

아래 예제는 Tool을 정의하고, 모델이 tool call을 내면 수동으로 실행한 뒤 최종 답을 생성한다.

```python
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

load_dotenv()

model = ChatOpenAI(
    model="solar-pro",
    base_url="https://api.upstage.ai/v1/solar",
    api_key=os.getenv("UPSTAGE_API_KEY"),
    temperature=0,
)

@tool
def search_tool(query: str) -> str:
    """최신 정보 또는 내부 지식 조회용 검색 도구"""
    print("search_tool 호출:", query)
    fake_db = {
        "김지윤": "김지윤은 예시 데이터에서 고객 지원 담당자로 등록되어 있습니다.",
        "환불": "환불은 결제 후 7일 이내, 미사용 상태에서 가능합니다.",
        "배송지연": "배송 지연 시 포인트 보상이 제공될 수 있습니다.",
    }

    for key, value in fake_db.items():
        if key in query:
            return value

    return "검색 결과 없음"


tools = [search_tool]
model_with_tools = model.bind_tools(tools)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "너는 고객지원 AI야. 모르는 정보 또는 최신 정보가 필요하면 반드시 search_tool을 사용해. "
        "절대 추측하지 마.",
    ),
    ("human", "{question}"),
])

chain = prompt | model_with_tools
query = "김지윤이 누구야?"

response = chain.invoke({"question": query})

if response.tool_calls:
    for tool_call in response.tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        if tool_name == "search_tool":
            tool_result = search_tool.invoke(tool_args)

            final_response = model.invoke([
                ("system", "검색 결과를 근거로만 답해. 모르면 모른다고 답해."),
                (
                    "human",
                    f"질문: {query}\n검색 결과: {tool_result}\n최종 답변 작성",
                ),
            ])
            print("최종 응답:", final_response.content)
else:
    print("도구 호출 없음:", response.content)
```

---

## 8. Agent 방식 예제 (자동 루프)

수동 루프 대신 AgentExecutor를 쓰면 도구 호출 루프를 자동화할 수 있다.

```python
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor

load_dotenv()

llm = ChatOpenAI(
    model="solar-pro",
    base_url="https://api.upstage.ai/v1/solar",
    api_key=os.getenv("UPSTAGE_API_KEY"),
    temperature=0,
)

@tool
def search_policy(query: str) -> str:
    """정책 문구를 조회한다."""
    policy = {
        "품절": "품절 보상은 주문 상태에 따라 포인트로 제공될 수 있습니다.",
        "총알배송": "총알배송 대상 상품은 지역/시간 조건에 따라 당일 또는 익일 배송됩니다.",
    }
    for k, v in policy.items():
        if k in query:
            return v
    return "관련 정책을 찾지 못했습니다."

prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 고객 지원 에이전트다. 필요한 경우 도구를 사용해라."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

tools = [search_policy]
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = executor.invoke({"input": "품절 보상제도 알려줘"})
print(result["output"])
```

---

## 9. RAG 기본 구조

RAG를 구현하려면 아래 5단계가 필요하다.

1. 문서 수집
2. 문서 분할(Chunking)
3. 임베딩 생성
4. 벡터스토어 저장
5. 질의 시 유사도 검색 + 답변 생성

---

## 10. RAG 전체 코드 (LangChain + HuggingFace Embedding)

아래 코드는 Day10 실습 구조를 반영한, "PDF 폴더 기반" RAG 파이프라인이다.

```python
import os
from glob import glob
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 1) 환경 로드
load_dotenv()
upstage_key = os.getenv("UPSTAGE_API_KEY")

# 2) LLM
llm = ChatOpenAI(
    model="solar-pro",
    base_url="https://api.upstage.ai/v1/solar",
    api_key=upstage_key,
    temperature=0,
)

# 3) 문서 로드
pdf_dir = r"day10_rag/실습/data"
pdf_files = glob(os.path.join(pdf_dir, "*.pdf"))

docs = []
for pdf in pdf_files:
    loader = PyPDFLoader(pdf)
    docs.extend(loader.load())

print(f"원본 문서 수: {len(docs)}")

# 4) 문서 분할
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=120,
)
chunks = splitter.split_documents(docs)
print(f"청크 수: {len(chunks)}")

# 5) 임베딩
emb = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",  # 다국어 성능 우수
    model_kwargs={"device": "cpu"},  # GPU 가능하면 "cuda"
)

# 6) 벡터스토어 구축
vector_db = FAISS.from_documents(chunks, emb)
retriever = vector_db.as_retriever(search_kwargs={"k": 3})

# 7) 프롬프트
prompt = ChatPromptTemplate.from_template(
    """
너는 고객센터 상담 AI야.
아래 [컨텍스트]에 있는 내용만 근거로 답해.
컨텍스트에 없으면 '문서에서 확인되지 않습니다'라고 답해.

[질문]
{question}

[컨텍스트]
{context}
""".strip()
)

def format_docs(documents):
    return "\n\n".join([d.page_content for d in documents])

# 8) RAG 체인
rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)

# 9) 테스트
question = "총알배송 혜택과 조건을 알려줘"
answer = rag_chain.invoke(question)
print(answer)
```

---

## 11. Chunking 전략 정리

Chunking은 RAG 품질의 핵심이다.

| 전략 | 장점 | 단점 |
|---|---|---|
| 큰 청크 | 문맥 유지 쉬움 | 불필요 텍스트 많아짐 |
| 작은 청크 | 검색 정밀도 좋음 | 문맥 끊김 가능 |
| overlap 증가 | 연결성 보완 | 중복 증가 |

실무 시작값(권장):

- `chunk_size`: 700~1200
- `chunk_overlap`: 80~180
- `k`: 3~5

---

## 12. Retriever 튜닝 포인트

1. `k`를 너무 낮추면 근거 부족.
2. `k`를 너무 높이면 노이즈 증가.
3. 질문 유형별로 `k`를 다르게 주는 전략이 효과적.
4. 메타데이터 필터(문서 출처, 날짜, 카테고리)를 붙이면 성능이 좋아진다.

---

## 13. LangGraph 기초 개념

LangChain LCEL이 직선형 파이프에 강하다면,
LangGraph는 아래 상황에서 강하다.

1. 조건 분기
2. 반복 루프
3. 상태 유지
4. 재시도/복구
5. 디버깅 가능한 노드 단위 실행

핵심 구성요소:

- State: 흐름 중 공유되는 상태 객체
- Node: 처리 함수
- Edge: 노드 연결
- START/END: 시작/종료

---

## 14. LangGraph로 RAG 구성 예제

```python
import os
from typing import TypedDict, List

from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI

# 이미 만든 retriever 재사용한다고 가정
# retriever = vector_db.as_retriever(search_kwargs={"k": 3})

load_dotenv()

llm = ChatOpenAI(
    model="solar-pro",
    base_url="https://api.upstage.ai/v1/solar",
    api_key=os.getenv("UPSTAGE_API_KEY"),
    temperature=0,
)

class RAGState(TypedDict):
    question: str
    contexts: List[str]
    answer: str


def retrieve_node(state: RAGState) -> RAGState:
    question = state["question"]
    docs = retriever.invoke(question)
    contexts = [d.page_content for d in docs]
    return {
        **state,
        "contexts": contexts,
    }


def generate_node(state: RAGState) -> RAGState:
    question = state["question"]
    context_text = "\n\n".join(state.get("contexts", []))

    msg = (
        "너는 고객센터 상담 AI다. 반드시 컨텍스트 근거로만 답해. "
        "컨텍스트에 없으면 모른다고 답해.\n\n"
        f"[질문]\n{question}\n\n"
        f"[컨텍스트]\n{context_text}"
    )
    resp = llm.invoke(msg)
    return {
        **state,
        "answer": resp.content,
    }


builder = StateGraph(RAGState)
builder.add_node("retrieve", retrieve_node)
builder.add_node("generate", generate_node)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

rag_graph = builder.compile()

result = rag_graph.invoke({
    "question": "도서 품절 보상제도 설명해줘",
    "contexts": [],
    "answer": "",
})

print(result["answer"])
```

---

## 15. LangSmith 필수 설정 및 사용 포인트

## 15-1. 설정

```env
LANGCHAIN_API_KEY=YOUR_LANGSMITH_KEY
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=day10-rag
```

## 15-2. 왜 중요한가

1. 어떤 문서가 검색됐는지 확인 가능
2. 프롬프트/모델 입력값 추적 가능
3. 실패 케이스 재현이 쉬움
4. A/B 실험과 평가 자동화 가능

## 15-3. 꼭 보는 항목

1. Retrieval 결과가 질문과 진짜로 관련 있는가
2. LLM 입력 context 길이가 과도하지 않은가
3. 정답인데 근거 없는 답변이 섞였는가
4. Tool 호출 루프가 과도하게 반복되는가

---

## 16. HuggingFace + Python으로 LLM 서버 직접 구성 (옵션)

아래는 OpenAI 호환 서버를 직접 띄우는 대표 흐름이다.

## 16-1. vLLM 서버 실행 예시

```bash
pip install vllm

python -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen2.5-7B-Instruct \
  --host 0.0.0.0 \
  --port 8000
```

## 16-2. LangChain에서 로컬 서버 호출

```python
from langchain_openai import ChatOpenAI

local_model = ChatOpenAI(
    model="Qwen/Qwen2.5-7B-Instruct",
    base_url="http://localhost:8000/v1",
    api_key="dummy",  # 로컬 서버는 형식상 값만 필요
    temperature=0,
)

print(local_model.invoke("RAG가 왜 필요한지 3줄로 설명해줘").content)
```

이렇게 하면 "모델 서버는 직접 운영 + RAG 파이프라인은 LangChain" 구조를 만들 수 있다.

---

## 17. Day10 실습/과제와 연결 포인트

현재 폴더 기준 핵심 자료:

1. `day10_rag/4-0_LangChain_실습.ipynb`
2. `day10_rag/4-0_LangGraph개요_solar_r1.ipynb`
3. `day10_rag/4-1_LangGraph와 RAG_r2.ipynb`
4. `day10_rag/실습/(실습-문제) 4-1_RAG_기반_Customer_Service_AI_에이전트_개발.ipynb`
5. `day10_rag/실습/(실습-힌트) 4-1_RAG_기반_Customer_Service_AI_에이전트_개발.ipynb`
6. `day10_rag/과제/(과제-문제) 4-1_RAG_기반_Customer_Service_AI_에이전트_개발.ipynb`
7. `day10_rag/과제/(과제-힌트) 4-1_RAG_기반_Customer_Service_AI_에이전트_개발.ipynb`

문서 데이터셋:

- `day10_rag/실습/data/*.pdf`
- `day10_rag/과제/data/*.pdf`

---

## 18. Notion에 붙일 때 권장 페이지 구조

아래 템플릿 그대로 복붙하면 페이지 구성 빠르다.

```md
# Day10 RAG 정리

## 1. 왜 RAG가 필요한가
- LLM 단독 한계
- Tool/Agent 필요성

## 2. 핵심 개념
- Embedding
- Vector Store
- Retriever
- Prompt Grounding

## 3. 구현 흐름
- 문서 로드
- 청킹
- 임베딩
- 벡터 저장
- 검색 + 생성

## 4. 코드 실습
- 기본 LangChain 체인
- Tool 호출
- RAG 파이프라인
- LangGraph 파이프라인

## 5. 디버깅
- LangSmith Tracing
- 실패 사례 분석

## 6. 튜닝
- chunk_size / overlap
- top-k
- 프롬프트 안전장치

## 7. 실무 적용 체크리스트
- 데이터 최신화
- 근거 기반 응답
- 실패 시 fallback
- 평가/모니터링
```

---

## 19. 실무형 품질 체크리스트

## 19-1. 기능 체크

1. 질문마다 관련 문서가 최소 1개 이상 검색되는가
2. 문서에 없는 내용은 "모름" 처리되는가
3. 답변에 근거 문장이 포함되는가
4. 응답 속도 SLA를 만족하는가

## 19-2. 데이터 체크

1. 오래된 문서가 섞여 있지 않은가
2. 중복 청크가 과도하지 않은가
3. PDF OCR 오류가 없는가
4. 메타데이터(출처, 날짜)가 관리되는가

## 19-3. 프롬프트 체크

1. 근거 없는 추측 금지 지시가 있는가
2. 답변 형식(표/목록/요약)이 일관적인가
3. 민감한 질문에 대한 안전 문구가 있는가

---

## 20. 자주 발생하는 문제와 해결

## 20-1. "엉뚱한 문서를 가져온다"

- chunk_size를 줄여본다.
- k를 3~5 사이로 재조정한다.
- 문서 전처리(헤더/푸터 제거)를 한다.
- 임베딩 모델을 바꿔본다.

## 20-2. "검색은 맞는데 답변이 틀린다"

- 프롬프트에 "컨텍스트 외 추측 금지"를 강제한다.
- 답변에 근거 문구 인용을 요구한다.
- temperature를 0에 가깝게 둔다.

## 20-3. "속도가 느리다"

- 임베딩/벡터 인덱스를 캐시한다.
- k를 줄인다.
- 모델 크기를 조정한다.
- 배치 처리 또는 비동기 처리를 적용한다.

---

## 21. 최종 정리

1. LLM 단독으로는 실무 정확도를 보장하기 어렵다.
2. Tool/Agent는 "행동 능력"을 확장한다.
3. RAG는 "지식 정확도"를 확장한다.
4. LangChain은 빠른 구현에 강하고,
5. LangGraph는 복잡 워크플로우에 강하며,
6. LangSmith는 운영 디버깅에 필수다.

Day10 핵심은 한 문장으로 정리된다.

**"모델 성능에만 의존하지 말고, 검색과 워크플로우를 설계해서 정확도를 만든다."**

---

## 22. 부록: 최소 실행 버전 (한 파일로 끝내기)

```python
import os
from glob import glob
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

# 1) LLM
llm = ChatOpenAI(
    model="solar-pro",
    base_url="https://api.upstage.ai/v1/solar",
    api_key=os.getenv("UPSTAGE_API_KEY"),
    temperature=0,
)

# 2) 문서 로드
pdf_files = glob("day10_rag/실습/data/*.pdf")
docs = []
for f in pdf_files:
    docs.extend(PyPDFLoader(f).load())

# 3) 청킹
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
chunks = splitter.split_documents(docs)

# 4) 임베딩 + 벡터스토어
emb = HuggingFaceEmbeddings(model_name="BAAI/bge-m3", model_kwargs={"device": "cpu"})
vdb = FAISS.from_documents(chunks, emb)
retriever = vdb.as_retriever(search_kwargs={"k": 3})

# 5) RAG 체인
prompt = ChatPromptTemplate.from_template(
    """
아래 문서를 근거로 질문에 답해.
문서에 없는 내용은 모른다고 답해.

질문: {question}
문서:
{context}
""".strip()
)

format_docs = lambda ds: "\n\n".join(d.page_content for d in ds)

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

while True:
    q = input("질문(종료: exit) > ").strip()
    if q.lower() == "exit":
        break
    print("\n답변:")
    print(chain.invoke(q))
    print("-" * 80)
```
