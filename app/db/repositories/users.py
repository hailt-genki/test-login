from typing import Optional

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.users import User, UserInDB


class UsersRepository(BaseRepository):
    async def get_user_by_email(self, *, email: str) -> UserInDB:
        user_row = await queries.get_user_by_email(self.connection, email=email)
        print(str(user_row))
        if user_row:
            resp = UserInDB(**user_row)
            resp.hashed_password = user_row['hashed_password']
            return resp
        raise EntityDoesNotExist("user with email {0} does not exist".format(email))

    async def get_user_by_username(self, *, username: str) -> UserInDB:
        user_row = await queries.get_user_by_username(
            self.connection,
            username=username,
        )
        if user_row:
            return UserInDB(**user_row)
        raise EntityDoesNotExist(
            "user with username {0} does not exist".format(username),
        )

    async def create_user(
        self,
        *,
        username: str,
        email: str,
        password: str,
    ) -> UserInDB:
        user = UserInDB(username=username, email=email)
        user.change_password(password)

        async with self.connection.transaction():
            user_row = await queries.create_new_user(
                self.connection,
                username=user.username,
                email=user.email,
                salt=user.salt,
                hashed_password=user.hashed_password,
            )

        return user.model_copy(update=dict(user_row))