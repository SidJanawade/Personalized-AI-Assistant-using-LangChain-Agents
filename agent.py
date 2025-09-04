import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import (
    get_candidate_info, schedule_interview, update_candidate_status,
    list_candidates_by_skill, remove_candidate,
    apply_leave, check_leave_status, approve_leave, reject_leave
)
from memory import get_memory

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5)

tools = [
    get_candidate_info, schedule_interview, update_candidate_status,
    list_candidates_by_skill, remove_candidate,
    apply_leave, check_leave_status, approve_leave, reject_leave
]

memory = get_memory()

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
)

def run_agent(query: str) -> str:
    return agent.run(query)
