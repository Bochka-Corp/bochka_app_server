from sqlalchemy import Column, UUID, Date, Float, Integer, Boolean
from sqlalchemy_imageattach.entity import image_attachment

from bochka.orm.baseclass import BaseClass
from bochka.orm.models.hotel import Hotel
from bochka.orm.models.room_type import RoomType


class RoomReservation(BaseClass):
    hotel_id = Column(UUID, Hotel.id, nullable=False)
    room_type_id = Column(UUID, RoomType.id, nullable=False)
    check_id_date = Column(Date, nullable=False)
    check_out_date = Column(Date, nullable=False)
    price_per_night = Column(Float, nullable=False)
    floor = Column(Integer, nullable=False)
    is_booked = Column(Boolean, nullable=False)
    guests_count = Column(Integer, nullable=False)

    picture = image_attachment("RoomImage")

