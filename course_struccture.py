from sqlmodel import Column, Field, Relationship, SQLModel
from typing import Optional, List

from datetime import datetime, timezone
from sqlalchemy import TIMESTAMP, func

from enum import Enum
from uuid import UUID, uuid4
from sqlalchemy.dialects.postgresql import UUID as PUUID


class Module(SQLModel, table=True):
    __tablename__ = "module"

    id: Optional[UUID] = Field(default_factory = uuid4,sa_column= Column(PUUID, primary_key=True, unique=True, default=uuid4, index = True))
    title: str = Field(unique = True, nullable = False)
    description: str = Field(nullable = False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now()))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc) ,sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now()), onupdate=func.now()) 

    course_id: UUID = Field(foreign_key="course.id")

    course: "Course" = Relationship(back_populates="modules")
    chapters: List["Chapter"] = Relationship(back_populates="module")


class Chapter(SQLModel, table=True):
    __tablename__ = "chapter"

    id: Optional[UUID] = Field(default_factory = uuid4,sa_column= Column(PUUID, primary_key=True, unique=True, default=uuid4, index = True))
    title: str = Field(unique = True, nullable = False)
    description: str = Field(nullable = False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now()))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc) ,sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now()), onupdate=func.now()) 


    module_id: UUID = Field(foreign_key="module.id")

    module: "Module" = Relationship(back_populates="chapters")
    lessons: List["Lesson"] = Relationship(back_populates="chapter")

class LessonContentType(str,Enum):
    Video = "video"
    Article = "article"
    Quiz = "quiz"
    Assignment = "assingnment"


class Lesson(SQLModel, table=True):
    __tablename__ = "lesson"
    
    id: Optional[UUID] = Field(default_factory = uuid4,sa_column= Column(PUUID, primary_key=True, unique=True, default=uuid4, index = True))
    title: str = Field(unique = True, nullable = False)
    content_type: LessonContentType = Field(nullable = False)
    content_url: str = Field(nullable = False)
    text_content: str = Field(nullable = False)
    duration_minutes: datetime = Field(default_factory = lambda : datetime.now(timezone.utc))

    chapter_id: int = Field(foreign_key="chapter.id")


    chapter: "Chapter" = Relationship(back_populates="lessons")
