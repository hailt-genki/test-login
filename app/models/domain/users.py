from typing import Optional

from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.rwmodel import RWModel
from app.services import security
import datetime


class User(RWModel):
    __tablename__ = 'users'
    username: str
    email: str
    image: str | None = None
    bio: str | None = None
    salt: str | None = None
    hashed_password: str | None = None
    id: int

class UserInDB(DateTimeModelMixin, User):
    # salt: str = ""
    # hashed_password: str = ""

    def check_password(self, password: str) -> bool:
        return security.verify_password(self.salt + password, self.hashed_password)

    def change_password(self, password: str) -> None:
        self.salt = security.generate_salt()
        self.hashed_password = security.get_password_hash(self.salt + password)
