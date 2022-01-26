from pydantic import BaseModel
from schema.getter_dict import PeeweeGetterDict


class ActorCreate(BaseModel):
    name: str
    age: int
    gender: str


class ActorSchema(ActorCreate):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict



