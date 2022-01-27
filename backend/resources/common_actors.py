from fastapi import APIRouter, status, HTTPException
from typing import List
from model.movie import Movie
from schema.actor import ActorSchema
from lib.utils import intersection
router = APIRouter(prefix='/common_actors', tags=["common_actors"])




# GET /common_actors?movies=string,string,...
#
# return
# 400 if at least one movie does not exist
# 422 if 'movies' query parameter does not exist
# 200
# Array<{
#     "name": string,
#     "age": number,
#     "gender": "male" | "female"
# }> (list of actors that appear in all requested movies)


@router.get("/", response_model=List[ActorSchema])
async def common_actors(movies: str):
    movies = movies.split(',')
    for movie_name in movies:
        movie = Movie.get_movie(movie_name)
        if not movie:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The movie {movie_name} does not exist")
    movies = Movie.select().where(Movie.title << movies)
    actors = [actor for actor in movies[0].actors]
    for movie in movies[1:]:
        aux = [actor for actor in movie.actors]
        actors = intersection(actors, aux)
    return actors
