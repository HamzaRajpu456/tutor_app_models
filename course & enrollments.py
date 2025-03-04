from enum import Enum 
from typing import List, Optional

from sqlmodel import Column, Field, Relationship, SQLModel

from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID as PUUID

class Category(str,Enum):
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    PHP = "php"


class CourseStatus(str, Enum):
    Draft = "draft"
    Published = "published"
    Archieved = "archieved"


class Course(SQLModel, table=True):
    __tablename__ = "course"

    id: Optional[UUID] = Field(default_factory = uuid4,sa_column=Column(PUUID, primary_key=True, unique=True, default=uuid4))
    title: str = Field(unique = True , nullable = False)
    description: str = Field(nullable = False)
    category: Category = Field(nullable = False) 
    price: float = Field(nullable = False)
    thumbnail: str = Field(nullable = False)
    status: CourseStatus = Field(nullable = False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now()))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc) ,sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now()), onupdate=func.now()) 

    teacher_id: UUID = Field(foreign_key="user.id")


    teacher: "User" = Relationship(back_populates = "course")
    modules: List["Module"] = Relationship(back_populates="course")



class CourseCompletionStatus(str, Enum):
    Active = "active"
    Completed = "completed"
    Dropped = "dropped"

class Enrollment(SQLModel, table=True):
    __tablename__ = "enrollment"

    user_id : Optional[UUID] = Field(primary_key = True, default_factory = None, index = True , foreign_key = "user.id") 
    course_id : Optional[UUID] = Field(primary_key = True, default_factory = None, index = True , foreign_key = "course.id")
    status : CourseCompletionStatus = Field(default = "active", nullable = False)
    enrollment_date : datetime = Field(default_factory = lambda : datetime.now(timezone.utc))
    completed_at : datetime = Field(default = None)


# Tasks
    # create pending schemas
    # expalin schema to me as beginer
    # how can i impeove it as sqlmodel and postgresql database as user can interact with databse usng sqlmodel but our data scientist can analyze data directly from pgadmin query tool
    # is this schema handle the default facotry functions for id and date and times in database query tool also 