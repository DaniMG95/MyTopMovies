from pydantic import BaseModel
from schena.getter_dict import PeeweeGetterDict


class MovieCreate(BaseModel):
    title: str
    category: str


class MovieSchema(MovieCreate):
    id: int
    actor_id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
