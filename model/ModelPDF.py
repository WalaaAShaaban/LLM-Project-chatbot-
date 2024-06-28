from langchain.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import sys
sys.path.append('/home/walaa-shaban/Documents/project/capston_llm_training/LLM-Project-chatbot/')
from model.LLM import LLM
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from src.embedding import embedding


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
        vector_database = Chroma.from_documents(documents=self.split_docs(),embedding=embedding(self.embed_model))
        retriever = vector_database.as_retriever(search_type=self.similarity,search_kwargs={"k":4})
        return retriever

    def __init__(self) -> None:
        self.retriver = self.vector_db()
        self.llm = Ollama(model="llama3:latest")