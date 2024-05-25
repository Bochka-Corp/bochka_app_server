from sqlalchemy import Column, UUID
from sqlalchemy.orm import relationship
from sqlalchemy_imageattach.entity import Image
from bochka.orm.baseclass import BaseClass
from bochka.orm.models.hotel import Hotel


class HotelImage(BaseClass, Image):
    hotel_id = Column(UUID, Hotel.id, nullable=False)
    hotel = relationship("Hotel", back_populates="hotel_images", cascade_backrefs=False)


class RoomImage(BaseClass, Image):
    room_id = Column(UUID, Hotel.id, nullable=False)
    room = relationship("Room", back_populates="room_images", cascade_backrefs=False)
