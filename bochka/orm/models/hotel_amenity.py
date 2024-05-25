from sqlalchemy import Column, Integer, Boolean

from bochka.orm.baseclass import BaseClass
from bochka.orm.models.amenity_type import AmenityType
from bochka.orm.models.hotel import Hotel


class HotelAmenity(BaseClass):
    __tablename__ = "hotel_amenity"

    hotel_id = Column(Integer, Hotel.id, nullable=False)
    amenity_type_id = Column(Integer, AmenityType.id, nullable=False)
    value = Column(Boolean, nullable=False)