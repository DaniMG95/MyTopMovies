from pydantic import BaseModel
from schema.getter_dict import PeeweeGetterDict


class ActorSchema(BaseModel):
    username: str
    password1: str
    password2: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


