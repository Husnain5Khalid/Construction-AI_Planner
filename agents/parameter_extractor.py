from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from config import GROQ_API_KEY, MODEL_NAME

from prompts.parameter_extractor import PARAMETER_EXTRACTION_PROMPT
from models.parameter_model import ToolParameters

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=0
)

structured_llm = llm.with_structured_output(ToolParameters)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", PARAMETER_EXTRACTION_PROMPT),
        ("human", "{question}")
    ]
)

extractor = prompt | structured_llm


def extract_parameters(question: str):

    return extractor.invoke(
        {
            "question": question
        }
    )