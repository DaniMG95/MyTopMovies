from pydantic import BaseModel
from typing import List
from schema.getter_dict import PeeweeGetterDict
from schema.actor import ActorSchema


class Movie(BaseModel):
    title: str
    category: str


class MovieCreate(Movie):
    cast: List[str]


class MovieSchema(Movie):
    id: int
    actors: List[ActorSchema]

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
