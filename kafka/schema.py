from pydantic import BaseModel
from sqlmodel import SQLModel

class Message(SQLModel):
    message : str
