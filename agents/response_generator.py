from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from config import GROQ_API_KEY, MODEL_NAME
from prompts.tool_response import TOOL_RESPONSE_PROMPT

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", TOOL_RESPONSE_PROMPT),
        (
            "human",
            """
Question:
{question}

Tool Result:
{result}
"""
        )
    ]
)

response_chain = prompt | llm


def generate_response(question: str, result: dict):

    response = response_chain.invoke(
        {
            "question": question,
            "result": result
        }
    )

    return response.content