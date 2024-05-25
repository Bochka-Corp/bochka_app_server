from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from bochka.orm.baseclass import BaseClass


class RoomType(BaseClass):
    type = Column(String, nullable=False)

    room_reservations = relationship("RoomReservation", back_populates="room_types", cascade_backrefs=False)

