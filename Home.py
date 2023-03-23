import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
path = 'projects/Company/'
st.title("The Best Company")
st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Cras erat dui, finibus vel lectus ac, pharetra dictum odio.
        Etiam risus sapien, auctor eu volutpat sit amet, porta in nunc.
        Quisque vitae varius ex, eu volutpat orci.""")
st.header("Our Team")

file = pd.read_csv("data.csv")
col1, col2, col3 = st.columns(3)

with col1:
    for index, row in file[:4].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.text(row['role'])
        st.image("images/"+row["image"])

with col2:
    for index, row in file[4:8].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.text(row['role'])
        st.image("images/"+row["image"])

with col3:
    for index, row in file[8:].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.text(row['role'])
        st.image("images/"+row["image"])
