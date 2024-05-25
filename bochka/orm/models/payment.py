from sqlalchemy import Column, UUID, DateTime, String, Float
from sqlalchemy_imageattach.entity import image_attachment

from bochka.orm.baseclass import BaseClass
from bochka.orm.models.booking import Booking


class Payment(BaseClass):
    booking_id = Column(UUID, Booking.id, nullable=False)
    payment_type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)


class PaymentReceipt(BaseClass):
    payment_id = Column(UUID, Payment.id, nullable=False)

    picture = image_attachment("ReceiptImage")
