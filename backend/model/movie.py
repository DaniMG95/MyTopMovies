from peewee import *
from db import BaseModel
from model.actor import Actor


class Movie(BaseModel):
    title = CharField()
    category = CharField()

    cast = ManyToManyField(Actor, backref="movies")

ActorsMovies = Movie.cast.get_through_model()