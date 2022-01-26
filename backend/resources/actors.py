from fastapi import APIRouter, HTTPException, Depends, status
from schema.actor import ActorSchema, ActorCreate
from model.actor import Actor
from typing import List
router = APIRouter(prefix='/actors', tags=["actors"])


# POST /actors
# {
#     "name": string,
#     "age": number,
#     "gender": "male" | "female"
# }
#
# return
# 422 is the body is malformed
# 400 if the actor's name already exists
# 400 if the actor's gender is not "male" or "female"
# 200
#
# if the request is succesful it should store the actor
@router.post("/", response_model=ActorSchema)
async def create_actor(actor: ActorCreate):
    if Actor.get_actor(actor.name):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"the actor's name already exists")
    elif actor.gender not in ["male", "female"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="the actor's gender is not 'male' or 'female'")
    else:
        actor = Actor.create_actor(actor)
        return actor


# GET / actors
#
# return
# 200
# Array < {
#     "name": string,
#     "age": number,
#     "gender": "male" | "female"
# } > (list of actors)

@router.get("/", response_model=List[ActorSchema])
async def get_actors():
    actores = Actor.get_all()
    return list(actores)
