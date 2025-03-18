from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

st.title("専門家選択型質問アプリ")
st.write("""
専門家の種類を選択し、入力した質問に対して専門家に応じた回答が表示されます。
""")

input_message = st.text_input(label="質問を入力してください:")
selected_item = st.radio(
    "専門家の種類を選択してください。",
    ["歴史", "科学"]
)

def get_llm_response(input_text, expert_type):
    if expert_type == "歴史":
        system_message = "You are a history expert. Provide detailed historical insights."
    elif expert_type == "科学":
        system_message = "You are a science expert. Provide detailed scientific explanations."
    else:
        system_message = "You are a helpful assistant."

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text)
    ]
    result = llm(messages)
    return result.content

if st.button("実行"):
    if input_message.strip():
        response = get_llm_response(input_message, selected_item)
        st.write("### 回答:")
        st.write(response)
    else:
        st.warning("質問を入力してください。")