from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # type: ignore


class ChapterORM(Base):  # type: ignore
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True)
    chapter_id = Column(String, nullable=False)
    number = Column(Integer)
    title = Column(String, nullable=False)
    create_at = Column(DateTime)
    project_id = Column(Integer, ForeignKey("projects.id"))
