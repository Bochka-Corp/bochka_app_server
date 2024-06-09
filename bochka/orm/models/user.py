from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy import Column, String, Integer, Date

from bochka.orm.models.baseclass import Base


class User(Base):
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    password_hash = Column(String, nullable=False)
    gender = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    birth_date = Column(Date, nullable=True)
    marital_status = Column(String, nullable=False, default=None)


