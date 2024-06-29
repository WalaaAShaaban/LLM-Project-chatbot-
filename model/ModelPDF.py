from langchain.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import sys
sys.path.append('/home/walaa-shaban/Documents/project/capston_llm_training/LLM-Project-chatbot/')
from model.LLM import LLM
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from src.embedding import embedding
from langchain_core.output_parsers import StrOutputParser
from langchain.tools import Tool

class ModelPDF:
    def input_doc(self):
        loader = PyPDFLoader('input/Introduction to Machine Learning with Python.pdf')
        pages = loader.load_and_split()
        return pages

    def get_llm(self):
        llm = LLM().get_llm()
        return llm

    def split_docs(self):
        text_splitters = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50, add_start_index=True)
        all_splits = text_splitters.split_documents(self.input_doc())
        return all_splits

    def vector_db(self):
        vector_database = Chroma.from_documents(documents=self.split_docs(),embedding=embedding())
        return vector_database
    
    def pdf_tool_function(self, input_data):
        query = input_data.get("query")
        return "Response from pdf_tool_function for query: {}".format(query)
    
    def create_pdf_agent(self,question:str):

        # tool_pdf = Tool(
        #     name="PDFTool",
        #     func=self.pdf_tool_function,
        #     description="Useful for when you want to answer questions about a PDF file",
        #     return_direct=True,
        #     output_parser=StrOutputParser(),
        # )
        agent = RetrievalQA.from_chain_type(llm=self.llm,
                                            chain_type="stuff",
                                            retriever=self.vector_db.as_retriever(),
                                            return_source_documents=True,
                                     
                                            ) 
           
        response = agent({"query": question})
        result = response['result']
        return result
        
    

    def __init__(self) -> None:
        self.vector_db = self.vector_db()
        self.llm = Ollama(model="llama3:latest")

        