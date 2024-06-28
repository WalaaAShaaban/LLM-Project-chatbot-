from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


class LLM:
    def get_llm(self) -> ChatGoogleGenerativeAI:
        load_dotenv()
        google_api_key = os.getenv('GEMINI_API_KEY')
        llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=google_api_key,temperature=0.7)
        return llm