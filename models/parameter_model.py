from pydantic import BaseModel
from typing import Optional

class ToolParameters(BaseModel):
    length : Optional[float] = None
    width : Optional[float] = None
    depth : Optional[float] = None
    height : Optional[float] = None

    
