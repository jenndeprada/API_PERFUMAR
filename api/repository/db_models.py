import uuid
from sqlalchemy import Column, ForeignKey, String, UniqueConstraint, Date, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.sqlalchemy import Base
from api.especies.infrastructure.repositories.postgres.models import Especie, Raza


class PGPerfume(Base):
    __tablename__ = 'perfumes'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    brand = Column(String(50), nullable=False)