from pydantic import BaseModel, Field


class ChapterModel(BaseModel):
    id: str
    number: int
    title: str
    create_at: str = Field(alias="createAt")

    class Config:
        orm_mode = True
