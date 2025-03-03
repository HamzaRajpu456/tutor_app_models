from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Module(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    course_id: int = Field(foreign_key="course.id")
    title: str
    description: Optional[str] = None
    position: int = Field(default=1)

    course: "Course" = Relationship(back_populates="modules")
    chapters: List["Chapter"] = Relationship(back_populates="module")


class Chapter(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    module_id: int = Field(foreign_key="module.id")
    title: str
    description: Optional[str] = None
    position: int = Field(default=1)

    module: "Module" = Relationship(back_populates="chapters")
    lessons: List["Lesson"] = Relationship(back_populates="chapter")


class Lesson(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    chapter_id: int = Field(foreign_key="chapter.id")
    title: str
    content_type: str  # Enum: video, article, quiz, assignment
    content_url: Optional[str] = None
    text_content: Optional[str] = None
    position: int = Field(default=1)
    duration_minutes: int = Field(default=10)

    chapter: "Chapter" = Relationship(back_populates="lessons")
