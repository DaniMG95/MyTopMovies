from peewee import *
import os


DATABASE = os.getenv('DATABASE')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))


mysql_db = MySQLDatabase(DATABASE, user=USER, password=PASSWORD,
                         host=HOST, port=PORT)

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = mysql_db