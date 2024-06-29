import sys
sys.path.append('/home/walaa-shaban/Documents/project/capston_llm_training/LLM-Project-chatbot/')
import streamlit as st
from streamlit_chat import message as st_message
from model.ModelCSV import ModelCSV
from model.ModelPDF import ModelPDF
from model.ModelDB import ModelDB


def get_response():
    user_message = st.session_state.chat_text
    st.session_state.history.append({"message": user_message, "is_user": True})
    
    
    #     result = ModelCSV().get_agent_csv().run(user_message)
    result = ModelPDF().create_pdf_agent(user_message)
    # model_db_instance = ModelDB()
    # agent_db = model_db_instance.create_db_agent()
    # result = agent_db.invoke({"input": user_message})['output']
    
    st.session_state.history.append({"message": result, "is_user": False})
    st.session_state.chat_text = ""
    
def main():
    st.set_page_config(page_title="Chatbot Application", page_icon=":robot_face:")
    st.header("Chatbot Application 📄 🛢️ 📚 ")
    

    if "history" not in st.session_state:
        st.session_state.history = []

    
    st.text_input("Enter your question ...",key="chat_text", on_change=get_response)
    for i, chat in enumerate(st.session_state.history):
        st_message(**chat, key=str(i))

if __name__ == "__main__":
    main()
