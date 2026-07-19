from typing import TypedDict, Optional


class ConstructionState(TypedDict):
    question: str
    route: str # this is planner
    tool_name: str | None
    tool_input: dict
    retrieved_documents: list # This is Rag
    tool_result: str | None # this is tool
    answer: str # this is LLm
 
