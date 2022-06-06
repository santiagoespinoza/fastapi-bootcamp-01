from typing import Optional
from pydantic import BaseModel


class HomeworkBase(BaseModel):
    title: str
    description: str

class HomeworkCreate(HomeworkBase):
    ower_id: int

class Homework(HomeworkBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True