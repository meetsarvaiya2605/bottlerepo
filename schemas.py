from datetime import datetime ,time
from pyexpat import model
from pydantic import BaseModel, EmailStr 
from typing import Optional , List


class UserCreate(BaseModel):
    username: str
    # bottle_id:int
    email_id :EmailStr
    firstname : str
    lastname : str
    hashed_password : str
    set_goal : int
    current_status : int
    notification_on : bool
    notification_off :bool

class UserResponse(BaseModel):
    id:int
    created_at: datetime

    class config:
        from_attribute:True



class BottleCreate(BaseModel):
    user_id:int
    bottle_capacity :int
    bottle_amount:int
class BottleResponse(BaseModel):
    id:int
    created_at:datetime
    class config :
        from_attribute:True