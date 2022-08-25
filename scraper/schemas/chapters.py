from pydantic import BaseModel


class Chapter(BaseModel):
    id: str
    number: int
    title: str
    created_at: str
