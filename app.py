import streamlit as st
import json
import google.generativeai as genai

# ファイルからデータを読み込む関数
def load_debate_data():
    with open("debate_data.json", "r", encoding="utf-8") as f:
        return json.load(f)
# API設定（環境変数などで管理）
genai.configure(api_key="AIzaSyA2B7Ae31pGl40y-5n11w3Kf469tbD1RcA")
st.title("🎓 ディベート・コーチング・ラボ")

# 1. 過去のディベートから選択
data = load_debate_data()
selected_debate = st.selectbox("分析したいディベートを選んでください", [d['theme'] for d in data])

if st.button("評価を開始する"):
    # 選択されたデータを取得
    target = next(d for d in data if d['theme'] == selected_debate)
    
    # AIへ分析を依頼
    model = genai.GenerativeModel('gemini-2.0-flash')
    prompt = f"以下のディベート内容を分析し、ユーザー側の論理的弱点と改善案を提示して：\n{target['history']}"
    
    response = model.generate_content(prompt)
    st.markdown("### 🏆 AIコーチの分析結果")
    st.write(response.text)