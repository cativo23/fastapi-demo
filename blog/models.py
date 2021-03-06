from .database import Base
from sqlalchemy import Column, Integer, String


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))
    body = Column(String(255))
