from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class CourseReview(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(foreign_key="studentprofile.id")
    course_id: int = Field(foreign_key="course.id")
    rating: int = Field(default=5)  # 1 to 5 stars
    review_text: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    student: "StudentProfile" = Relationship()
    course: "Course" = Relationship()
