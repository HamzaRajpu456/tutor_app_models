from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class Course(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    teacher_id: int = Field(foreign_key="teacherprofile.id")
    title: str
    description: Optional[str] = None
    category: str
    price: float = Field(default=0.0)
    thumbnail: Optional[str] = None
    status: str = Field(default="draft")  # Enum: draft, published, archived
    created_at: datetime = Field(default_factory=datetime.utcnow)

    teacher: "TeacherProfile" = Relationship()
    modules: List["Module"] = Relationship(back_populates="course")


class Enrollment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(foreign_key="studentprofile.id")
    course_id: int = Field(foreign_key="course.id")
    enrollment_date: datetime = Field(default_factory=datetime.utcnow)
    progress: int = Field(default=0)  # Percentage
    status: str = Field(default="active")  # Enum: active, completed, dropped

    student: "StudentProfile" = Relationship()
    course: "Course" = Relationship()
