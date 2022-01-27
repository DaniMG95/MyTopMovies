from fastapi import APIRouter, HTTPException, Depends, status
from lib.utils import intersection
from schema.movie import MovieSchema
from typing import List
from model.actor import Actor
router = APIRouter(prefix='/performances', tags=["performances"])

# GET /performances?actors=string,string,...
#
# return
# 400 if at least one of the actors does not exist
# 422 if the 'actors' query parameter is not sent
# 200
# Array<{
#     "title": string,
#     "category": string,
#     "cast": Array<string>
# }> (list of movies where all the actors in the query appear)


@router.get("/", response_model=List[MovieSchema])
async def common_actors(actors: str):
    actors = actors.split(',')
    for actor_name in actors:
        actor = Actor.get_actor(actor_name)
        if not actor:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The actor {actor_name} does not exist")
    actors = Actor.select().where(Actor.name << actors)
    movies = [movie for movie in actors[0].movies]
    for actor in actors[1:]:
        aux = [movie for movie in actor.movies]
        movies = intersection(movies, aux)
    return [movie.serialize() for movie in movies]
