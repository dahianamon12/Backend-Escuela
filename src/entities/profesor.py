import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.database.config import Base


class Profesor(Base):
    _tablename_ = "profesor"

    id_profesor = Column(
        UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), primary_key=True
    )
    especialidad = Column(String(150))
    id_departamento = Column(
        UUID(as_uuid=True), ForeignKey("departamento.id_departamento")
    )

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())
    id_usuario_creacion = Column(
        UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=False
    )
    id_usuario_edita = Column(
        UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=True
    )

    usuario_creacion = relationship("Usuario", foreign_keys=[id_usuario_creacion])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])
    departamento = relationship("Departamento", foreign_keys=[id_departamento])
