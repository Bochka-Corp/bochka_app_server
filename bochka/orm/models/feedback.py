from sqlalchemy import Column, UUID, Text, Integer, ForeignKey
from bochka.orm.models.baseclass import Base
from bochka.orm.models.hotel import Hotel
from bochka.orm.models.user import User


class Feedback(Base):
    user_id = Column(UUID, ForeignKey(User.id), nullable=False)
    hotel_id = Column(UUID, ForeignKey(Hotel.id), nullable=False)
    text = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
