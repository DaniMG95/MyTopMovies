from pydantic import BaseModel
from fastapi import Query
from schema.getter_dict import PeeweeGetterDict


class User(BaseModel):
    name: str
    username: str
    email: str = Query(..., regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    password: str = Query(..., min_length=4)

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


