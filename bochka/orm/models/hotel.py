from sqlalchemy import Column, String, Float, Text, UUID, ForeignKey
from sqlalchemy.orm import relationship

from bochka.orm.models.baseclass import Base
from bochka.orm.models.admin import Admin


class Hotel(Base):
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
    hotel_admin_id = Column(UUID, ForeignKey(Admin.id), nullable=False, default=None)

    hotel_amenities = relationship("HotelAmenity", back_populates="hotels", cascade_backrefs=False)
    hotel_room_reservations = relationship("RoomReservation", back_populates="hotels", cascade_backrefs=False)