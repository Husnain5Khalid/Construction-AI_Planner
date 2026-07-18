from typing import TypedDict, Optional


class ConstructionState(TypedDict):
    question: str

    route: str

    tool_name: Optional[str]

    tool_input: dict

    retrieved_documents: list

    tool_result: Optional[str]

    answer: str

    