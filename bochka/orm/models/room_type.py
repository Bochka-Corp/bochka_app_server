from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from bochka.orm.models.baseclass import Base


class RoomType(Base):
    type = Column(String, nullable=False)

    room_reservations = relationship("RoomReservation", back_populates="room_types", cascade_backrefs=False)

