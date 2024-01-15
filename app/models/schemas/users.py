from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl
from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.users import User
from app.models.schemas.rwschema import RWSchema


class UserInLogin(RWSchema):
    email: EmailStr
    password: str

class UserWithToken(User):
    token: str


class UserInResponse(RWSchema):
    user: UserWithToken

class UserInCreate(UserInLogin):
    username: str

class UserInUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[HttpUrl] = None