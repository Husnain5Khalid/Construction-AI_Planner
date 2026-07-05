'''
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    api_key = GROQ_API_KEY,
    model = MODEL_NAME,
)

response = llm.invoke("Explain M30 concrete in simple words.")
print(response.content)

'''

from planner import route_question

questions = [
    
    "What is OPC cement?",

    "What is AI",

    "What is the beam size in Drawing A101?",

    "Calculate paint required for a 10m × 3m wall."

    "Summarize our contract document."

    "What is the weather tomorrow?"

    "Estimate bricks for a 20 ft wall."
]

for q in questions:

    result = route_question(q)
    print("=" * 40)
    print(q)
    print(result)
