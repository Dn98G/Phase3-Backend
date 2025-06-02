from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True

class NoteBase(BaseModel):
    title: str
    content: Optional[str] = None
    is_archived: Optional[bool] = False

class NoteCreate(NoteBase):
    tags: Optional[List[str]] = []

class Note(NoteBase):
    id: int
    created_at: datetime
    updated_at: datetime
    tags: List[Tag]

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True