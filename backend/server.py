from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from db import mysql_db
from resources import actors, movies, common_actors, performances, users
from model import actor, movie, user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(actors.router)
app.include_router(movies.router)
app.include_router(common_actors.router)
app.include_router(performances.router)
app.include_router(users.router)


@app.on_event("startup")
def before_request():
    if mysql_db.is_closed():
        mysql_db.connect()
    mysql_db.create_tables([actor.Actor, movie.Movie, movie.Movie.actors.get_through_model(), user.User])

@app.on_event("shutdown")
def after_request(response):
    mysql_db.close()
    return response