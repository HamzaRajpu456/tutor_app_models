from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class TeacherProfile(SQLModel, table=True):
    __tablename__ = "teacher"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True)
    bio: Optional[str] = None
    qualification: Optional[str] = None
    experience_years: int = Field(default=0)
    profile_picture: Optional[str] = None
    rating: float = Field(default=0.0)
    
    user: "User" = Relationship()


class StudentProfile(SQLModel, table=True):
    __tablename__ = "student"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", unique=True)
    enrollment_date: datetime = Field(default_factory=datetime.utcnow)
    profile_picture: Optional[str] = None

    user: "User" = Relationship()
