from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(foreign_key="studentprofile.id")
    course_id: int = Field(foreign_key="course.id")
    amount: float
    payment_method: str  # Enum: credit_card, paypal, stripe
    status: str  # Enum: pending, successful, failed
    transaction_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    student: "StudentProfile" = Relationship()
    course: "Course" = Relationship()
