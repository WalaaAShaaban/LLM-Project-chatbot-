import sys
sys.path.append('/home/walaa-shaban/Documents/project/capston_llm_training/LLM-Project-chatbot/')
import streamlit as st
from streamlit_chat import message as st_message
from langchain.agents import tool
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType, load_tools
import PyPDF2
import csv
from model.LLM import LLM
from langchain.llms import Ollama
from langchain.callbacks import StreamlitCallbackHandler

# Define the PDF reading tool
@tool
def read_pdf(file_path: str) -> str:
    """Reads text from a PDF file."""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfFileReader(f)
        text = ""
        for page_num in range(reader.getNumPages()):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

# Define the CSV reading tool
@tool
def read_csv(file_path: str) -> str:
    """Reads data from a CSV file."""
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return "\n".join([", ".join(row) for row in data])


# llm = LLM().get_llm()
llm = Ollama(model="llama3:latest")

math_tools = load_tools(['llm-math'], llm=llm)
tools = [read_pdf, read_csv] + math_tools
memory = ConversationBufferMemory(memory_key="chat_history")

conversational_agent = initialize_agent(
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=7,
    memory=memory
)


def get_response():
    user_message = st.session_state.chat_text
    st.session_state.history.append({"message": user_message, "is_user": True})
    response = conversational_agent.run(user_message)
    st.session_state.history.append({"message": response, "is_user": False})
    st.session_state.chat_text = ""

    
    
def main():
    st.set_page_config(page_title="Chatbot Application", page_icon=":robot_face:")
    st.header("Chatbot Application 📄 🛢️ 📚 ")
    

    if "history" not in st.session_state:
        st.session_state.history = []

    
    st.text_input("Enter your question ...",key="chat_text", on_change=get_response)
    # if prompt := st.chat_input():
    #     st.chat_message("user").write(prompt)
    #     with st.chat_message("assistant"):
            
    for i, chat in enumerate(st.session_state.history):
        st_message(**chat, key=str(i))

if __name__ == "__main__":
    main()
