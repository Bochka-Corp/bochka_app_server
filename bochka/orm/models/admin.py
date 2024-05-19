from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy import Column, String

from bochka.orm.baseclass import BaseClass


class Admin(BaseClass):
    __tablename__ = "admins"

    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

    def set_password(self, password):
        self.password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password_hash)
