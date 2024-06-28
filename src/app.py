import streamlit as st
from streamlit_chat import message as st_message

st.header("Chatbot Application 📄 🛢️ 📚")
if "history" not in st.session_state:
    st.session_state.history = []


def get_response():
    user_message = st.session_state.chat_text
    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": f"you are asked {user_message}", "is_user": False})
    st.session_state.chat_text = ""
    


st.text_input("Enter your question ...",key="chat_text", on_change=get_response)

for i, chat in enumerate(st.session_state.history):
    st_message(**chat, key=str(i))
 