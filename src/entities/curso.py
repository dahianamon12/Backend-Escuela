import uuid

from sqlalchemy import Column, DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.database.config import Base


class Curso(Base):
    __tablename__ = "curso"

    id_curso = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    nombre_curso = Column(String(100), nullable=False)
    descripcion = Column(Text)
    horas_semanales = Column(String(20))
    id_profesor = Column(UUID(as_uuid=True), ForeignKey("profesor.id_profesor"))
    id_grado = Column(UUID(as_uuid=True), ForeignKey("grado.id_grado"))
    id_aula = Column(UUID(as_uuid=True), ForeignKey("aula.id_aula"))

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
    profesor = relationship("Profesor", foreign_keys=[id_profesor])
    grado = relationship("Grado", foreign_keys=[id_grado])
    aula = relationship("Aula", foreign_keys=[id_aula])
