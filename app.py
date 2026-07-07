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

#from planner import route_question
'''

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
'''
'''
from tools.weather import get_weather

print(get_weather("dammam"))

'''
# Execute the tool
'''
from planner import route_question
from tools.executor import execute_tool
'''
'''
from planner import route_question
from agents.tool_agent import ToolAgent

question = "Calculate concrete volume"

decision = route_question(question)

print(decision)

if decision.route == "tool":

    tool_agent = ToolAgent()

    tool = tool_agent.run(question)

    print(tool)

'''
'''
from agents.tool_agent import ToolAgent

agent = ToolAgent()

result = agent.run(
    "Calculate concrete for a slab 10m x 5m x 0.15m"
)

print(result)
'''

from agents.tool_agent import ToolAgent
from planner import route_question
from agents.tool_agent import ToolAgent

question = "Calculate concrete for 10m x 5m x 0.15m"

decision = route_question(question)
print(decision)

if decision.route == "tool":
    agent = ToolAgent()
    result = agent.run(question)
    print(result)