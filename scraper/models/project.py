from pydantic import BaseModel


class ProjectModel(BaseModel):
    project_id: int
    name: str
    adult: bool
    description: str
    cover: str
    create_at: str
    update_at: str

    class Config:
        orm_mode = True
