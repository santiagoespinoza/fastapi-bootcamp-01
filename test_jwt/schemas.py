from re import S
from pydantic import BaseModel

class AuthDetails(BaseModel):
    username: str
    password: str