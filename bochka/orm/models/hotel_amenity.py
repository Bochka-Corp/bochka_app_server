from sqlalchemy import Column, Boolean, ForeignKey, UUID

from bochka.orm.models.baseclass import Base
from bochka.orm.models.amenity_type import AmenityType
from bochka.orm.models.hotel import Hotel


class HotelAmenity(Base):
    hotel_id = Column(UUID, ForeignKey(Hotel.id), nullable=False)
    amenity_type_id = Column(UUID, ForeignKey(AmenityType.id), nullable=False)
    value = Column(Boolean, nullable=False)