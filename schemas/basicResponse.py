from pydantic import BaseModel
from typing import Optional

class BasicResponse(BaseModel):
    status: bool
    message: Optional[str]