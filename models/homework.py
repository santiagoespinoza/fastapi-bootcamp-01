from matplotlib.pyplot import title
from pandas import describe_option
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.db import Base

class Homework(Base):
    __tablename__ = 'home_works'

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, index = True)
    description = Column(String, index = True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates = 'home_works')