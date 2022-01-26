from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
router = APIRouter(prefix='/movies', tags=["movies"])
from schema.movie import MovieCreate, MovieSchema
from model.movie import Movie
from model.actor import Actor


# POST /movies
# {
#     "title": string,
#     "category": string,
#     "cast": Array<string>
# }
#
# return
# 422 if the body is malformed
# 400 if movie's title already exists
# 400 if at least one of the actors in the cast is not registered
# 200 if correct
#
# if the request is successful it should store the movie


@router.post("/", response_model=MovieSchema)
def create_movie(movie: MovieCreate):
    if Movie.get_movie(movie.title):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"the movie's name already exists")
    for actor_name in movie.cast:
        actor = Actor.get_actor(actor_name)
        if actor is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"the actor {actor_name} in the cast is not registered")
    Movie.create_movie(movie)
    new_movie = Movie.get_movie(movie.title)
    for actor_name in movie.cast:
        actor = Actor.get_actor(actor_name)
        actor.movies.add(new_movie)
    return new_movie


# GET / movies
#
# return
# 200
# Array < {
#     "title": string,
#     "category": string,
#     "cast": Array < string >
# } > (list of movie titles)
@router.get("/", response_model=List[MovieSchema])
def get_movie():
    movies = Movie.get_all()
    return list(movies)

