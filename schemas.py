from datetime import datetime, time
from pyexpat import model
from pydantic import BaseModel, EmailStr
from typing import Optional, List


class UserCreate(BaseModel):
    username: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    password: Optional[str] = None
    notification_on: Optional[bool] = None
    notification_off: Optional[bool] = None
    email_id: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    created_at: datetime
    last_drink_time: datetime

    class config:
        from_attribute: True


class Token(BaseModel):
    access_token: str
    token_type: str


class BottleCreate(BaseModel):
    # user_id:int
    bottle_capacity: int
    bottle_amount: int


class BottleResponse(BaseModel):
    id: int
    bottle_capacity: int
    bottle_amount: int
    created_at: datetime

    class config:
        from_attribute: True


class GoalSet(BaseModel):
    set_goal: int


class GoalResponse(BaseModel):
    id: int
    user_id: int
    created_at: datetime

    class config:
        from_attribute: True
