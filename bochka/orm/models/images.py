# from sqlalchemy import Column, UUID
# from sqlalchemy.orm import relationship
# from sqlalchemy_imageattach.entity import Image
# from bochka.orm.models.baseclass import Base
# from bochka.orm.models.hotel import Hotel
# from bochka.orm.models.payment import PaymentReceipt
# from bochka.orm.models.user import User
#
#
# class HotelImage(Base, Image):
#     hotel_id = Column(UUID, Hotel.id, nullable=False)
#     hotel = relationship("Hotel", back_populates="hotel_images", cascade_backrefs=False)
#
#
# class RoomImage(Base, Image):
#     room_id = Column(UUID, Hotel.id, nullable=False)
#     room = relationship("Room", back_populates="room_images", cascade_backrefs=False)
#
#
# class UserImage(Base, Image):
#     user_id = Column(UUID, User.id, nullable=False)
#     user = relationship("User", back_populates="user_images", cascade_backrefs=False)
#
#
# class ReceiptImage(Base, Image):
#     receipt_id = Column(UUID, PaymentReceipt.id, nullable=False)
#     receipt = relationship("PaymentReceipt", back_populates="receipt_images", cascade_backrefs=False)
