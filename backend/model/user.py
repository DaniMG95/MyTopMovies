from peewee import *
from db import BaseModel
from schema.user import User

class User(BaseModel):
    username = CharField()
    name = CharField()
    email = CharField()
    password = CharField()


    @classmethod
    def create_user(cls, user: User):
        user = cls(username=user.username, name=user.name, email=user.email, password=user.password)
        user.save()
        return user

    @classmethod
    def is_exist_username(cls, user: User):
        try:
            cls.get(cls.username == user.username)
            return True
        except:
            return False
