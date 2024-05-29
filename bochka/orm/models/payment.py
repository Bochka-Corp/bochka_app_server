from sqlalchemy import Column, UUID, DateTime, String, Float, ForeignKey
# from sqlalchemy_imageattach.entity import image_attachment

from bochka.orm.models.baseclass import Base
from bochka.orm.models.booking import Booking


class Payment(Base):
    booking_id = Column(UUID, ForeignKey(Booking.id), nullable=False)
    payment_type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)


class PaymentReceipt(Base):
    payment_id = Column(UUID, ForeignKey(Payment.id), nullable=False)

    # picture = image_attachment("ReceiptImage")
