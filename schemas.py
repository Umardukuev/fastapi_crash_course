from pydantic import BaseModel, ConfigDict
from typing import Optional

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STaskRead(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskID(BaseModel):
    ok: bool = True
    task_id: int