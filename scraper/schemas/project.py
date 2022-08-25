from datetime import datetime
from pydantic import BaseModel
from .chapters import Chapter

class Project(BaseModel):
    id: int
    name: str
    adult: bool
    description: str
    cover: str
    createAt: datetime
    updateAt: datetime
    # chapters: list[Chapter]
