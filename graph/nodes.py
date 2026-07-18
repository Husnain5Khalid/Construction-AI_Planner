from agents.planner import route_question
from graph.state import ConstructionState
from agents.llm_agent import LLMAgent

#Wrapping planner agent
def planner_node(state: ConstructionState):
    decision = route_question(state["question"])
    state["route"] = decision.route
    return state

#Router Function(which Route is this)
def route_decision(state: ConstructionState):
    return state["route"]


# Wrap the  LLM Agent

llm = LLMAgent()

def llm_node(state: ConstructionState):

    state["answer"] = llm.run(
        state["question"]
    )

    return state


# Wrap the Tool Agent

from agents.tool_agent import ToolAgent

tool = ToolAgent()


def tool_node(state: ConstructionState):

    state["answer"] = tool.run(
        state["question"]
    )

    return state


# Wrap RAG Agent

from rag.rag_agent import RAGAgent

rag = RAGAgent()


def rag_node(state: ConstructionState):

    state["answer"] = rag.run(
        state["question"]
    )

    return state





