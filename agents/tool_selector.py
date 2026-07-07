from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from config import GROQ_API_KEY, MODEL_NAME
from prompts.tool_selector import TOOL_SELECTOR_PROMPT
from models.tool_model import ToolSelection


llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)

structured_llm = llm.with_structured_output(ToolSelection)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", TOOL_SELECTOR_PROMPT),
        ("human", "{question}")
    ]
)

tool_selector = prompt | structured_llm


def select_tool(question: str):
    return tool_selector.invoke(
        {
            "question": question
        }
    )