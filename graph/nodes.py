from graph.state import ConstructionState
from agents.planner import route_question

# pLanner node

def planner_node(state: ConstructionState):

    decision = route_question(state["question"])

    state["route"] = decision.route

    return state

# LLM Node
from agents.llm_agent import LLMAgent

llm = LLMAgent()


def llm_node(state):

    prompt = f"""
Question:
{state["question"]}

Retrieved Documents:
{state["retrieved_documents"]}

Tool Result:
{state["tool_result"]}

Generate a helpful final answer.
"""

    state["answer"] = llm.run(prompt)

    return state

# Tool Node

from agents.tool_agent import ToolAgent

tool_agent = ToolAgent()


def tool_node(state: ConstructionState):

    state["answer"] = tool_agent.run(state["question"])

    return state

# RAG Node
from rag.rag_agent import RAGAgent

rag = RAGAgent()


def rag_node(state: ConstructionState):

    answer = rag.run(state["question"])

    state["answer"] = answer

    return state

# Router Function
def route_decision(state: ConstructionState):

    return state["route"]

