from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class Quiz(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    lesson_id: int = Field(foreign_key="lesson.id")
    title: str
    total_marks: int

    lesson: "Lesson" = Relationship()


class Question(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    quiz_id: int = Field(foreign_key="quiz.id")
    question_text: str
    question_type: str  # Enum: MCQ, True/False, Short Answer

    quiz: "Quiz" = Relationship()
