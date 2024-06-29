from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.llms import Ollama
from langchain.agents import create_sql_agent

class ModelDB:

    answer_prompt = PromptTemplate.from_template("""
            Given the following user question, corresponding SQL query, and the SQL result, answer the user question.

            Question: {question}
            SQL Query: {query}
            SQL Result: {result}

            Answer: 
            """)
    
    def create_db_agent(self):
        tool_db = Tool(
            name="SQLDatabase",
            func=self.db.run,
            description="Useful for when you want to answer questions about a database",
            return_direct=True,
            output_parser=StrOutputParser(),
        )
        agent = create_sql_agent(
            db=self.db, 
            llm=self.llm,
            tool=tool_db,
            verbose=True,
        )
        return agent

    def __init__(self):
        self.llm = Ollama(model="llama3:latest")
        self.db = SQLDatabase.from_uri("sqlite:///input/Chinook.db")


    