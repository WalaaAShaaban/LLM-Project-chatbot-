
from langchain.llms import Ollama
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent
from langchain.agents.agent_types import AgentType

class ModelCSV:

    def __init__(self):
        self.llm = Ollama(model="llama3:latest")
        

    def get_agent_csv(self):
        agent = create_csv_agent(self.llm, 
                                 'input/NvidiaDocumentationQandApairs.csv', 
                                 verbose=True, AgentType=AgentType.ZERO_SHOT_REACT_DESCRIPTION
                                 )
        return agent
    
    
