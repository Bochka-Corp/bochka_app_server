from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy import Column, String, Float, Text, ForeignKey, UUID

from bochka.orm.baseclass import BaseClass
from bochka.orm.models.admin import Admin


class Hotel(BaseClass):
    __tablename__ = "hotels"

    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    street = Column(String, nullable=False)
    house_number = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    hotel_admin_id = Column(UUID, Admin.id, nullable=False, default=None)
