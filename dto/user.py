from pydantic import BaseModel
from fastapi import UploadFile

class User(BaseModel):
    name:str
    last_name: str
    age: int

class UserMultipart(BaseModel):
    name: str
    last_name: str
    age: int
    profile_picture: UploadFile