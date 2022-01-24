from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from db import mysql_db
from resources import actors, movies, common_actors, performances




app = FastAPI()

app.include_router(actors.router)
app.include_router(movies.router)
app.include_router(common_actors.router)
app.include_router(performances.router)


@app.on_event("startup")
def before_request():
    if mysql_db.is_closed():
        mysql_db.connect()

@app.on_event("shutdown")
def after_request(response):
    mysql_db.close()
    return response