
from pydantic import BaseModel, Field
from typing import Optional
'''
class PlannerDecision(BaseModel):
    route: str
    tool_name: Optional[str] = None
    reason: str
'''
#upper coment out funcion follow before step7 in lesson 3. After step 6 it is updated

class PlannerDecision(BaseModel):
    route: str
    tool_name: Optional[str] = None
    tool_input: dict = Field(default_factory=dict) #default_factory=Whenever a new PlannerDecision object is created, call dict() to make a brand-new empty dictionary.
    reason: str
