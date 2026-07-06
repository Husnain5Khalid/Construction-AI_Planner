from typing import Literal
from pydantic import BaseModel

class ToolSelection(BaseModel):
    tool_name: Literal[
        "concrete_calculator",
        "brick_estimator",
        "weather",
        "none",
    ]


'''Why use Literal?

If we use:

tool_name: str

the model might return:

calculator

or

calc_tool

or

concrete tool

All of those would fail because they don't match our registry.

With Literal, the LLM is constrained to the exact allowed values.'''

