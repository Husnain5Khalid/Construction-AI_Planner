
from pydantic import BaseModel
from typing import Optional

class PlannerDecision(BaseModel):
    route: str
    tool_name: Optional[str] = None
    reason: str
