from sqlalchemy import Column, UUID, DateTime, String, ForeignKey

from bochka.orm.models.baseclass import Base
from bochka.orm.models.hotel import Hotel
from bochka.orm.models.user import User


class Booking(Base):
    user_id = Column(UUID, ForeignKey(User.id), nullable=False)
    hotel_id = Column(UUID, ForeignKey(Hotel.id), nullable=False)
    check_in_date = Column(DateTime, nullable=False)
    check_out_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    booking_source = Column(String, nullable=False)