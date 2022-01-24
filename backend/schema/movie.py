from pydantic import BaseModel
from schena.getter_dict import PeeweeGetterDict


class MovieCreate(BaseModel):
    name: str
    rating: float


class MovieSchema(MovieCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
