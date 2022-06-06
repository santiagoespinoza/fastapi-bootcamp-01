from typing import List
from pydantic import BaseModel
from schemas.homework import Homework

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password:str

class User(UserBase):
    id: int
    is_Active: bool
    home_works: List[Homework] = []

    class Config:
        orm_mode = True