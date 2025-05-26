import streamlit as st

st.title("용우중")

# 예제 1: 간단한 설명 숨기기
with st.expander("🔍 설명 보기"):
    st.write("""
        이 애플리케이션은 사용자의 입력을 기반으로 데이터를 필터링하고 시각화합니다.
        아래의 항목들을 입력하면 실시간으로 결과가 변경됩니다.
    """)

# 예제 2: 여러 줄 텍스트 입력 숨기기
with st.expander("✍️ 메모 입력"):
    note = st.text_area("여기에 학습 내용을 메모하세요")

# 예제 3: 데이터프레임 숨기기

import pandas as pd

df = pd.DataFrame({
    "과목": ["수학", "영어", "과학"],
    "점수": [90, 85, 95]
})
with st.expander("점수표 보기"):
    st.dataframe(df)
