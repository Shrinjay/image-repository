from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    s3_key = Column(String)
    city = Column(String)
    country = Column(String)
    objects = Column(String)
