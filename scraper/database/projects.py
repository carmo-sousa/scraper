from typing import TypeAlias

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base: TypeAlias = declarative_base()  # type: ignore


class ProjectORM(Base):  # type: ignore
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer)
    name = Column(String, nullable=False)
    adult = Column(Boolean, default=False)
    description = Column(String)
    cover = Column(String)
    create_at = Column(DateTime)
    update_at = Column(DateTime)
