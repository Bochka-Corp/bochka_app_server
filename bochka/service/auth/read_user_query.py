from sqlalchemy import select
from sqlalchemy.orm import Session

from bochka.service.schemas.user import UserLogin
from bochka.orm.models.user import User
from bochka.utils.crypto import verify_password


class ReadUserQuery:
    def __init__(self, user: UserLogin, session: Session):
        self.user = user
        self.session = session

    def login(self) -> bool:
        query = select(User).where(User.email == self.user.email)

        user: User = self.session.execute(query).scalar()

        return verify_password(self.user.password, user.password_hash)
