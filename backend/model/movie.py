from peewee import *
from db import BaseModel
from schema.movie import MovieSchema
from model.actor import Actor


class Movie(BaseModel):
    title = CharField()
    category = CharField()
    actors = ManyToManyField(Actor, backref='movies')

    def serialize(self):
        # front end does not need user ID here
        return {
            'title': self.title,
            'category': self.category,
            'cast': [actor.name for actor in self.actors]
        }

    @classmethod
    def create_movie(cls, movie: MovieSchema):
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

