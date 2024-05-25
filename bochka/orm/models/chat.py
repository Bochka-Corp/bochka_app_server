from sqlalchemy import Column, UUID, String, Text, DateTime, Boolean
from bochka.orm.baseclass import BaseClass
from bochka.orm.models.hotel import Hotel
from bochka.orm.models.user import User


class Chat(BaseClass):
    user_id = Column(UUID, User.id)
    hotel_id = Column(UUID, Hotel.id)


class ChatMessage(BaseClass):
    chat_id = Column(UUID, Chat.id)
    sender_type = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    is_read = Column(Boolean, nullable=False)
