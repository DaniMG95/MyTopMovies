from pydantic import BaseModel
from typing import List


class Movie(BaseModel):
    title: str
    category: str


class MovieSchema(Movie):
    cast: List[str]
