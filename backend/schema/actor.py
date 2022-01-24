from pydantic import BaseModel
from schema.getter_dict import PeeweeGetterDict


class ActorSchema(BaseModel):
    name: str
    age: int
    gender: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


