from db.connection import Base
from sqlalchemy import Column, Integer, String, Boolean
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    profile_picture = Column(String)
    is_active = Column(Boolean, default=True)