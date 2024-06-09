from sqlalchemy import insert
from sqlalchemy.orm import Session

from bochka.service.schemas.user import UserRegister
from bochka.orm.models.user import User
from bochka.utils.crypto import set_password


class CreateUserCommand:
    def __init__(self, user: UserRegister, session: Session):
        self.user = user
        self.session = session

    def execute(self) -> None:
        user = self.user.model_dump()
        user["password_hash"] = set_password(user["password"])
        del user["password"]
        command = insert(User).values(self.user.model_dump())

        self.session.execute(command)
