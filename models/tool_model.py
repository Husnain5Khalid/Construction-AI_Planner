from typing import Literal
from pydantic import BaseModel


class ToolSelection(BaseModel):
    tool_name: Literal[
        "concrete_calculator",
        "brick_estimator",
        "weather",
        "none"
    ]