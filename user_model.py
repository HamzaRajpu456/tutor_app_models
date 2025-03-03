from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    password_hash: str
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    roles: List["UserRole"] = Relationship(back_populates="user")

class Role(SQLModel, table=True):
    __tablename__ = "role"
  
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)

    users: List["UserRole"] = Relationship(back_populates="role")

class UserRole(SQLModel, table=True):
    __tablename__ = "userrole"

    user_id: int = Field(foreign_key="user.id", primary_key=True)
    role_id: int = Field(foreign_key="role.id", primary_key=True)

    user: "User" = Relationship(back_populates="roles")
    role: "Role" = Relationship(back_populates="users")