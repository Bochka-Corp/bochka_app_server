import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, UUID, MetaData
from sqlalchemy.ext.declarative import as_declarative, declared_attr

metadata = MetaData()


@as_declarative(metadata=metadata)
class Base:
    id = Column(UUID, primary_key=True, default=uuid.uuid4, nullable=False)

    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    deleted_at = Column(DateTime, default=None, nullable=False)
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
