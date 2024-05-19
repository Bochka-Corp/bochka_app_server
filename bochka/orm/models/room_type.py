from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship

from bochka.orm.baseclass import BaseClass


class RoomType(BaseClass):
    __tablename__ = "room_types"

    type = Column(String, nullable=False)

    room_reservations = relationship("RoomReservation", back_populates="room_types", cascade_backrefs=False)

