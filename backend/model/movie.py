from peewee import *
from db import BaseModel
from schema.movie import MovieCreate
from model.actor import Actor


class Movie(BaseModel):
    title = CharField()
    category = CharField()
    actors = ManyToManyField(Actor, backref='movies')


    @classmethod
    def create_movie(cls, movie: MovieCreate):
        movie = cls(title=movie.title, category=movie.category)
        movie.save()
        return movie

    @classmethod
    def get_movie(cls, title: str):
        try:
            movie = Movie.get(title=title)
            return movie
        except:
            return None

    @classmethod
    def get_all(cls):
        try:
            return cls.select()
        except:
            return None

