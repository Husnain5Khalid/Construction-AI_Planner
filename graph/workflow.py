from langgraph.graph import StateGraph, START, END

from graph.state import ConstructionState
from graph.nodes import (
    planner_node,
    tool_node,
    rag_node,
    llm_node,
    route_decision
)

builder = StateGraph(ConstructionState)

builder.add_node("planner", planner_node)
builder.add_node("tool", tool_node)
builder.add_node("rag", rag_node)
builder.add_node("llm", llm_node)

# connect the graph
builder.add_edge(
    START,
    "planner"
)

builder.add_conditional_edges(
    "planner",
    route_decision,
    {
        "tool": "tool",
        "rag": "rag",
        "llm": "llm"
    }
)

builder.add_edge("tool", "llm")
builder.add_edge("rag", "llm")
builder.add_edge("llm", END)

graph = builder.compile()

