from langgraph.graph import StateGraph
from langgraph.graph import START, END

from graph.state import ConstructionState

from graph.nodes import (
    planner_node,
    tool_node,
    rag_node,
    llm_node,
    route_decision
)

# create Builder
builder = StateGraph(
    ConstructionState
)

# Add Nodes

builder.add_node(
    "planner",
    planner_node
)

builder.add_node(
    "tool",
    tool_node
)

builder.add_node(
    "rag",
    rag_node
)

builder.add_node(
    "llm",
    llm_node
)

# Add Start

builder.add_edge(
    START,
    "planner"
)

# Add Conditional Edge
builder.add_conditional_edges(
    "planner",
    route_decision,
    {
        "tool": "tool",
        "rag": "rag",
        "llm": "llm"
    }
)

# Add END
builder.add_edge(
    "tool",
    END
)

builder.add_edge(
    "rag",
    END
)

builder.add_edge(
    "llm",
    END
)

#Compile
graph = builder.compile()

