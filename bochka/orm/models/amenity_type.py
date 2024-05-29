from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from bochka.orm.models.baseclass import Base


class AmenityType(Base):
    name = Column(String, nullable=False)

    hotel_amenities = relationship("HotelAmenity", back_populates="amenity_types", cascade_backrefs=False)