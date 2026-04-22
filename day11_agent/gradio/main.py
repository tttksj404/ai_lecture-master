from typing_extensions import TypedDict, Annotated
import operator
import os

from langchain.chat_models import init_chat_model
from langchain_upstage import ChatUpstage  # Upstage

from langchain.messages import AnyMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver # InMemorySaver : 세션별 데이터를 저장하기 위한 기능
from dotenv import load_dotenv

# ===== LLM =====
load_dotenv() # .env파일에서 환경설정 가져오기

# OpenAI API는 아래 주석을 풀고 쓰세요.
#llm = init_chat_model("gpt-5-nano", temperature=0)

# Upstage API는 아래 주석을 풀고 쓰세요.
llm = ChatUpstage(model="solar-pro", upstage_api_key=os.getenv("UPSTAGE_API_KEY"), temperature=0)


# ===== State =====
class State(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]


# ===== Node =====
def BBQ(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


# ===== Graph 구성 =====
graph = StateGraph(State)
graph.add_node("BBQ", BBQ)
graph.add_edge(START, "BBQ")
graph.add_edge("BBQ", END)

agent = graph.compile()


# ===== 단기기억 메모리 추가 ======
checkpointer = InMemorySaver() # checkpointer = 저장공간
agent = graph.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "user1"}} # user1님의 대화이력으로 저장할 예정



# ===== 실행(동작 테스트) =====
#result = agent.invoke({"messages": [HumanMessage(content="KFC랑 맥도날드 치킨 중 뭐가 더 맛있지? 한줄 요약")]})

#for m in result["messages"]:
#    m.pretty_print()

import gradio as gr
from langchain_core.messages import HumanMessage


# 1. 채팅 처리 함수
def chat(user_input, history):
    # LangGraph 실행 (입력값 전달)
    result = agent.invoke(
        {"messages": [HumanMessage(content=user_input)]},
        config={"configurable": {"thread_id": "user_1"}}
    )

    ai_reply = result["messages"][-1].content

    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": ai_reply})
    return history, ""


# 2. UI 구성
with gr.Blocks() as demo:
    gr.Markdown("### 🍗 LangGraph 챗봇")

    with gr.Row():
        # --- 왼쪽: 입력 영역 ---
        with gr.Column(scale=1):
            msg = gr.Textbox(
                label="질문 입력",
                placeholder="내 이름은 KFC, 탐정이죠 제 이름을 기억해주세요.",
                lines=3
            )
            submit_btn = gr.Button("🚀 전송", variant="primary")

        # --- 오른쪽: 대화 이력 (높이 400) ---
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(label="대화 이력", height=400)

    # 이벤트 연결 (엔터 및 버튼 클릭)
    msg.submit(chat, [msg, chatbot], [chatbot, msg])
    submit_btn.click(chat, [msg, chatbot], [chatbot, msg])

# 3. Gradio 실행
demo.launch(share=True)