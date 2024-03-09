from fastapi import APIRouter
from pydantic import BaseModel
from server.tables.user import User

class SignUpUser(BaseModel) :
    name: str
    email: str 
    password: str
    
class LoginUser(BaseModel) :
    email: str 
    password: str

router = APIRouter(prefix="/user")

@router.post("/create")
async def create_user(user: SignUpUser):
    user = User.add_user(user.name,user.email,user.password)
    if not user :
        return {
            "status" : "Error",
            "message" : "User already exists"
        }
    return {
        "status" : "Success",
        "message" : user
    }
    
    
    
@router.post("/login")
async def login_user(user: LoginUser):
    get_user = User.get_user(user.email,user.password)
    if not get_user :
        return {
            "status" : "Error",
            "message" : "Not a valid user"
        }
    return {
        "status" : "Success",
        "message" : get_user
    }
    
    
    





    


