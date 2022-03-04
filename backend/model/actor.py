from peewee import *
from db import BaseModel
from schema.actor import ActorCreate


class Actor(BaseModel):
    username = CharField()
    name = CharField()
    age = IntegerField()
    gender = CharField()

    @classmethod
    async def create_actor(cls, actor: ActorCreate):
        actor = cls(name=actor.name, age=actor.age, gender=actor.gender)
        await actor.save()
        return actor

    @classmethod
    async def get_actor(cls, actor_name: str):
        try:
            return await cls.get(Actor.name == actor_name)
        except:
            return None

    @classmethod
    async def get_all(cls):
        try:
            return await cls.select()
        except:
            return None