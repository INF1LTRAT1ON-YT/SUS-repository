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
<link href="https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Pacifico&family=Roboto:wght@400;500&display=swap" rel="stylesheet">

<style>
/* 본문: Gowun Dodum(한글), Roboto(영문) */
html, body, [class*="css"] {
  font-family: 'Gowun Dodum', 'Roboto', system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.7;   /* 손글씨 느낌은 줄간격을 넉넉히 */
}

/* 제목: Pacifico (영문), 한글 제목도 Gowun Dodum이 자연스러움 */
h1, h2 {
  font-family: 'Pacifico', 'Gowun Dodum', cursive;
  letter-spacing: 0.5px;
}
h1 { font-size: 2.0rem; }
h2 { font-size: 1.4rem; }

/* 본문 굵게/기울임도 손글씨 톤을 해치지 않게 최소 사용 권장 */
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
