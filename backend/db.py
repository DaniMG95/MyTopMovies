import peewee
from contextvars import ContextVar
from const import DATABASE, USER, PASSWORD, HOST, PORT

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


mysql_db = peewee.MySQLDatabase(DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)

mysql_db._state = PeeweeConnectionState()

class BaseModel(peewee.Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = mysql_db

