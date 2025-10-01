import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(page_title="INF1LTRAT1ON's Homepage", page_icon="🚀", layout="centered")

# 제목
st.title("🚀 My First Homepage (made by INF1LTRAT1ON)")
st.write("this is just a homepage nothing to see lol")

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">

<style>
/* 앱 전체에 폰트 적용 */
html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# 간단한 데이터프레임
st.header("My Favorites")
df = pd.DataFrame({
    "category": ["song", "movie", "game", "language"],
    "-": ["Imposter - Sightless in Shadow","K-Pop Demon Hunters","Arras.io","English or spanish"]
})
st.dataframe(df)


# 버튼 이벤트
if st.button("Click button"):
    st.success("Why are you still here?")

url = "https://i.ibb.co/FqWTknbC/Running-dictionary-1-star.png"
# 이미지 표시
st.image(url, caption="my 31,780,475 score in vocab.com ")
