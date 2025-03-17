from dotenv import load_dotenv
load_dotenv()

"""
「app.py」にコードを記述してください。
画面に入力フォームを1つ用意し、入力フォームから送信したテキストをLangChainを使ってLLMにプロンプトとして渡し、回答結果が画面上に表示されるようにしてください。なお、当コースのLesson8を参考にLangChainのコードを記述してください。
ラジオボタンでLLMに振る舞わせる専門家の種類を選択できるようにし、Aを選択した場合はAの領域の専門家として、またBを選択した場合はBの領域の専門家としてLLMに振る舞わせるよう、選択値に応じてLLMに渡すプロンプトのシステムメッセージを変えてください。また用意する専門家の種類はご自身で考えてください。
「入力テキスト」と「ラジオボタンでの選択値」を引数として受け取り、LLMからの回答を戻り値として返す関数を定義し、利用してください。
Webアプリの概要や操作方法をユーザーに明示するためのテキストを表示してください。
Streamlit Community Cloudにデプロイする際、Pythonのバージョンは「3.11」としてください。
"""

"""
Run Command
streamlit run sample1.py
"""

import streamlit as st
st.title("サンプルアプリ①: 簡単なWebアプリ")
input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")
text_count = len(input_message)
if st.button("実行"):
    st.write(f"文字数: **{text_count}**")
