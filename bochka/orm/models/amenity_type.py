from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship

from bochka.orm.baseclass import BaseClass


class AmenityType(BaseClass):
    __tablename__ = "amenity_types"

    name = Column(String, nullable=False)

    hotel_amenities = relationship("HotelAmenity", back_populates="amenity_types", cascade_backrefs=False)