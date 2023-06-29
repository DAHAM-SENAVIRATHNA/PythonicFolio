import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        <style>
        img {
            border-radius: 50%;
            object-fit: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.image("images/profile.png", width=450)
with col2:
    st.title("Nayana Senavirathna")

