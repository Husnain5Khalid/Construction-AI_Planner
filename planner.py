from langchain_core.prompts import ChatPromptTemplate
from config import GROQ_API_KEY, MODEL_NAME
from langchain_groq import ChatGroq

from prompts.planner import PLANNER_SYSTEM_PROMPT
from models.planner_model import PlannerDecision

llm = ChatGroq(
    api_key = GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)

structured_llm = llm.with_structured_output(PlannerDecision)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", PLANNER_SYSTEM_PROMPT),
        ("human", "{question}")
    ]
)



planner = prompt | structured_llm  # | called LangChain Expression Language (LCEL). It creates a pipeline.

def route_question(question: str):
    decision = planner.invoke(
        {
            "question": question
        }
    )

    return decision

#user:
#Calculate concrete volume
# then 
#route_question(question)
# then 
#ChatPromptTemplate

#System:
#You are Planner...

#Human:
#Calculate concrete volume

