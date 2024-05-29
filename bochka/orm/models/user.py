from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy import Column, String, Integer, Date
# from sqlalchemy_imageattach.entity import image_attachment

from bochka.orm.models.baseclass import Base


class User(Base):
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    birth_date = Column(Date, nullable=False)
    marital_status = Column(String, nullable=False, default=None)

    # picture = image_attachment("UserImage")

    def set_password(self, password):
        self.password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password_hash)
