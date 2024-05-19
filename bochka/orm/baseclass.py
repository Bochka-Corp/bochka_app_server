import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseClass(Base):
    id = Column(UUID, primary_key=True, default=uuid.uuid4, nullable=False)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    deleted_at = Column(DateTime, default=None, nullable=False)

