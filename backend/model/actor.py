from peewee import *
from db import BaseModel


class Actor(BaseModel):
    name = CharField()
    age = IntegerField()
    gender = CharField()