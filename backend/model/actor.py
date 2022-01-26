from peewee import *
from db import BaseModel
from schema.actor import ActorCreate, ActorSchema


class Actor(BaseModel):
    name = CharField()
    age = IntegerField()
    gender = CharField()

    @classmethod
    def create_actor(cls, actor: ActorCreate):
        actor = cls(name=actor.name, age=actor.age, gender=actor.gender)
        actor.save()
        return actor

    @classmethod
    def get_actor(cls, actor_name: str):
        try:
            return cls.get(Actor.name == actor_name)
        except:
            return None

    @classmethod
    def get_all(cls):
        try:
            return cls.select()
        except:
            return None