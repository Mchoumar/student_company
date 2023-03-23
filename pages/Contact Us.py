import streamlit as st
from send_email import email_send
import pandas as pd
df = pd.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    user_select = st.selectbox("What topic do you want to discuss?",
                               df["topic"])
    raw_message = st.text_area("Text")
    message = f"""\
    To: To MAHMOUD CHOUMAR\n
    From: New message form {user_email}\n
    Subject: {user_select}\n
    {raw_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        email_send(message)
        st.success('This is a success message!', icon="✅")