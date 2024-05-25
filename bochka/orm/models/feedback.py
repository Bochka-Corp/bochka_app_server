from sqlalchemy import Column, UUID, Text, Integer
from bochka.orm.baseclass import BaseClass
from bochka.orm.models.hotel import Hotel
from bochka.orm.models.user import User


class Feedback(BaseClass):
    user_id = Column(UUID, User.id, nullable=False)
    hotel_id = Column(UUID, Hotel.id, nullable=False)
    text = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
