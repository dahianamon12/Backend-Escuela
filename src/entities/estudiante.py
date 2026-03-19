import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.database.config import Base


class Estudiante(Base):
    __tablename__ = "estudiante"

    id_estudiante = Column(
        UUID(as_uuid=True), ForeignKey("usuario.id_usuario"), primary_key=True
    )
    direccion = Column(String(255))
    telefono = Column(String(20))
    fecha_nacimiento = Column(DateTime)
    id_grado = Column(UUID(as_uuid=True), ForeignKey("grado.id_grado"))

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
    grado = relationship("Grado", foreign_keys=[id_grado])
    usuario = relationship("Usuario", foreign_keys=[id_estudiante])