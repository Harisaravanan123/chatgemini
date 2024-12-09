import streamlit as st
import google.generativeai as genai
st.set_page_config(page_title='genAI',page_icon=":robot_face:",layout='wide')
api_key="AIzaSyDoxrT4DQkCwo4Dx6f3kugeHSW2mnXW0wI"
genai.configure(api_key=api_key)
model=genai.GenerativeModel('gemini-pro')
prompt=st.chat_input("enter a prompt:")
if prompt is not None:
    response=model.generate_content(prompt)
    st.write(response.text)