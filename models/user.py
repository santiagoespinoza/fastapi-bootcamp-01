import email
from enum import unique
from click import password_option
from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String, unique = True, index = True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default = True)

    home_works = relationship('Homework', back_populates = True)