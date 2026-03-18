import datetime
from uuid import UUID

from src.database.config import SessionLocal

from entities.asistencia import Asistencia

db = SessionLocal()


def crear_asistencia(
    fecha: datetime,
    estado: str,
    id_estudiante: UUID,
    id_curso: UUID,
    id_usuario_creacion: UUID,
) -> Asistencia:
    asistencia = Asistencia(
        fecha=fecha,
        estado=estado,
        id_estudiante=id_estudiante,
        id_curso=id_curso,
        id_usuario_creacion=id_usuario_creacion,
    )
    db.add(asistencia)
    db.commit()
    db.refresh(asistencia)
    return asistencia
