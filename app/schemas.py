from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class NoteBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)


class NoteCreate(NoteBase):
    pass


class NoteUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    content: Optional[str] = Field(None, min_length=1)


class Note(NoteBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr = Field(..., description="User email address")
    username: str = Field(..., min_length=3, max_length=50, description="Username for login")
    full_name: Optional[str] = Field(None, max_length=100, description="User's full name")


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, description="User password")


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = Field(None, description="User email address")
    username: Optional[str] = Field(None, min_length=3, max_length=50, description="Username for login")
    full_name: Optional[str] = Field(None, max_length=100, description="User's full name")
    password: Optional[str] = Field(None, min_length=8, description="User password")
    is_active: Optional[bool] = Field(None, description="Whether the user account is active")


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True