from fastapi import APIRouter
from models.User import User,Roles
from fastapi import Depends
from services import UserService
from fastapi.security import  OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/users",
    tags=["User"],   
    responses={404: {"description": "Not found"}},
)

@router.get('',summary='Get the user')
def register() -> User:
    return User(username="vishal",role=Roles.Admin)

@router.post('',summary='Register the user')
def register(user:User) :
    print(user)
    return {'message':'user registered succesfully'}



@router.post("/token", response_model=UserService.Token,summary="Generate user token by providing username and password" )
async def GenerateToken(form_data: OAuth2PasswordRequestForm = Depends()):

    access_token = UserService.GenerateToken(form_data.username, form_data.password)     
    return  UserService.Token(token_type="bearer", access_token=access_token)



@router.get("/me/", response_model=User)
async def read_users_me(current_user: User = Depends(UserService.get_current_active_user)):
    return current_user


@router.get("/me/items/")
async def read_own_items(current_user: User = Depends(UserService.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]