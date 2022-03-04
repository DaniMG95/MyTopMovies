from fastapi import HTTPException, APIRouter, status
from starlette.status import HTTP_400_BAD_REQUEST
from schema.user import User
from model.user import User as UserModel
from lib.security import get_password_hash


router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User, response_model_exclude=["password"])
async def create_user(user: User):
    user_exist = UserModel.is_exist_username(user)
    if user_exist:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST)
    user.password = get_password_hash(user.password)
    user_db = UserModel.create_user(user)
    return user_db
