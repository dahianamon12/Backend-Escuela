import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.database.config import Base


class Calificacion(Base):
    _tablename_ = "calificacion"

    id_calificacion = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    nota = Column(String(10))
    fecha = Column(DateTime)
    id_estudiante = Column(UUID(as_uuid=True), ForeignKey("estudiante.id_estudiante"))
    id_curso = Column(UUID(as_uuid=True), ForeignKey("curso.id_curso"))

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
    estudiante = relationship("Estudiante", foreign_keys=[id_estudiante])
    curso = relationship("Curso", foreign_keys=[id_curso])
