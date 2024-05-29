from sqlalchemy import Column, UUID, String, Text, DateTime, Boolean, ForeignKey
from bochka.orm.models.baseclass import Base
from bochka.orm.models.hotel import Hotel
from bochka.orm.models.user import User


class Chat(Base):
    user_id = Column(UUID, ForeignKey(User.id))
    hotel_id = Column(UUID, ForeignKey(Hotel.id))


class ChatMessage(Base):
    chat_id = Column(UUID, ForeignKey(Chat.id))
    sender_type = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    is_read = Column(Boolean, nullable=False)
