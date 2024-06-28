import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from sentence_transformers import SentenceTransformer
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
from langchain.agents.agent_types import AgentType

import sys
sys.path.append('/home/walaa-shaban/Documents/project/capston_llm_training/LLM-Project-chatbot/')
from model.LLM import LLM


class ChatModel:

    docs = ['input/NvidiaDocumentationQandApairs.csv',
            'input/Introduction to Machine Learning with Python.pdf',
            '/home/walaa-shaban/Documents/project/capston_llm_training/LLM-Project-chatbot-/input/Chinook.db']
  
    def __init__(self):
        self.llm = LLM().get_llm()
        print(f"LLM Type: {type(self.llm)}")  # Debug print

    def input_doc(self):
        loader = PyPDFLoader(self.docs[1])
        pages = loader.load_and_split()
        return pages
    
    

    def get_agent_csv(self):
        df = pd.read_csv(self.docs[0])
        print(f"DataFrame Info: {df.info()}")  # Debug print
        agent = create_pandas_dataframe_agent(
            llm=self.llm,
            df=df,
            max_execution_time=60,
            max_iterations=50,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            allow_dangerous_code=True  # Add this line to enable the functionality
        )
        print(f"Agent Type: {type(agent)}")  # Debug print
        return agent
    
    
