import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, empty, col2 = st.columns([1, 0.2, 2])
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

    st.image("images/profile.png", width=350)
    st.header("Contact")
    content3 = """
    E-mail:   nayanads2000@gmail.com\n
    linkedin: https://www.linkedin.com/in/nayana-senavirathna-6964941b3/
    """
    st.write(content3)

with col2:
    st.title("Nayana Senavirathna")

    st.markdown(
        """
        <style>
        .text-justify {
            text-align: justify;
            text-justify: inter-word;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    content1 = """
     Welcome to my portfolio!\n
     I am an ambitious and dedicated undergraduate student pursuing a 
     Bachelor of Information and Communication Technology (BICT) degree at the University of Kelaniya, specializing in the 
     Software System pathway. This portfolio showcases my skills, projects, and achievements as I embark on a journey to become a 
     proficient software developer.
    """

    content2 = """
    1. Programming Languages: HTML5, CSS3, JavaScript, Python, Kotlin, PL/SQL
    2. Web Development: Front-End Development, Back-End Development, Version Control (Git)
    3. Frameworks & Libraries: React, Bootstrap
    4. Database Systems: MySQL, MongoDB, Oracle Database
    5. Problem-Solving: Analytical Thinking, Troubleshooting, Debugging
    6. Collaboration: Teamwork, Communication, Adaptability
    """

    st.info(content1)
    st.subheader("Skills")
    st.write(content2)

content3 = "projects "
st.header(content3)

col3, empty, col4 = st.columns([2, 0.5, 2])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:2].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[2:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.write(f"[source code]({row['url']})")

