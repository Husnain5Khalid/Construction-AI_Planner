from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    api_key = GROQ_API_KEY,
    model = MODEL_NAME,
)

response = llm.invoke("Explain M30 concrete in simple words.")
print(response.content)
