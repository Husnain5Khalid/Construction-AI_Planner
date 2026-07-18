from typing import TypedDict

from langgraph.graph import StateGraph #when information travelled between node, it is stored in State, we say that it is StateGraph
from langgraph.graph import START,END

# Create the State

class GraphState(TypedDict):
    question: str 
    answer : str

# Creating the First Node

def greeting_node(state: GraphState):
    question = state["question"]
    state["answer"] = f"Hello! You said: {question}"


    return state

# Create the Graph

builder = StateGraph(GraphState)


# Add the Node

builder.add_node(
    "greetings",
    greeting_node  #The graph contains one node named: greeting  whose implementation is: greeting_node
)

#connect start
# Every graph begins somewhere.

builder.add_edge(
    START,
    "greetings"
)

# connect end: Now tell LangGraph where execution finishes.

builder.add_edge(
    "greetings",
    END
)

#Compile the Graph
graph = builder.compile() #It does not execute the graph. It validates the workflow and creates an executable graph.

# Execute the Graph
result = graph.invoke(
    {
        "question": "Hello",
        "answer": ""
    }


)
print(result)