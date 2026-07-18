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





