import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from sentence_transformers import SentenceTransformer
from langchain.llms import Ollama
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent
from langchain.agents.agent_types import AgentType

import sys
sys.path.append('/home/walaa-shaban/Documents/project/capston_llm_training/LLM-Project-chatbot/')
from model.LLM import LLM


class ModelCSV:

    docs = ['input/NvidiaDocumentationQandApairs.csv',
            'input/Introduction to Machine Learning with Python.pdf',
            '/home/walaa-shaban/Documents/project/capston_llm_training/LLM-Project-chatbot-/input/Chinook.db']
  
    def __init__(self):
        self.llm = Ollama(model="llama3:latest")
        
    
    

    def get_agent_csv(self):
        agent = create_csv_agent(self.llm, 'input/NvidiaDocumentationQandApairs.csv', verbose=True)
        return agent
    
    
