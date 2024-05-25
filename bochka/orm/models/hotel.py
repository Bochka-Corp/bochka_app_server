from sqlalchemy import Column, String, Float, Text, UUID
from sqlalchemy.orm import relationship
from sqlalchemy_imageattach.entity import image_attachment

from bochka.orm.baseclass import BaseClass
from bochka.orm.models.admin import Admin


class Hotel(BaseClass):
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    street = Column(String, nullable=False)
    house_number = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    hotel_admin_id = Column(UUID, Admin.id, nullable=False, default=None)

    picture = image_attachment("HotelImage")

    hotel_amenities = relationship("HotelAmenity", back_populates="hotels", cascade_backrefs=False)
    hotel_room_reservations = relationship("RoomReservation", back_populates="hotels", cascade_backrefs=False)