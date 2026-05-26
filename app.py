import streamlit as st
import json

# データの読み込み
def load_data():
    with open("debate_library.json", "r", encoding="utf-8") as f:
        return json.load(f)

st.title("🏆 ディベート・ライブラリ")

data = load_data()

# 選択UI
theme_list = [d['theme'] for d in data]
selected_theme = st.selectbox("学習したいテーマを選択:", theme_list)

# データ表示
target = next(d for d in data if d['theme'] == selected_theme)

st.subheader(f"テーマ: {target['theme']}")
st.write(f"あなたの立場: {target['user_stance']}")

# ディベート内容の吹き出し表示
for chat in target['debate_history']:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

# 評価の表示
st.divider()
st.subheader("💡 AIコーチからの評価")
st.metric("スコア", target['ai_evaluation']['score'])
st.info(f"評価: {target['ai_evaluation']['feedback']}")
st.success(f"次へのヒント: {target['ai_evaluation']['advice']}")