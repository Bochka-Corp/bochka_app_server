from sqlalchemy import Column, UUID, DateTime, String

from bochka.orm.baseclass import BaseClass
from bochka.orm.models.hotel import Hotel
from bochka.orm.models.user import User


class Booking(BaseClass):
    user_id = Column(UUID, User.id, nullable=False)
    hotel_id = Column(UUID, Hotel.id, nullable=False)
    check_in_date = Column(DateTime, nullable=False)
    check_out_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    booking_source = Column(String, nullable=False)