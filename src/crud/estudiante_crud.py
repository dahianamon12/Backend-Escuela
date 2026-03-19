from typing import Optional
from uuid import UUID

from src.database.config import SessionLocal

from src.entities.estudiante import Estudiante

def crear_estudiante(
    id_usuario: UUID, id_grado: UUID, id_usuario_creacion: UUID, **kwargs
) -> Estudiante:
    db = SessionLocal()
    try:
        estudiante = Estudiante(
            id_estudiante=id_usuario,
            id_grado=id_grado,
            id_usuario_creacion=id_usuario_creacion,
            **kwargs
        )
        db.add(estudiante)
        db.commit()
        db.refresh(estudiante)
        return estudiante
    finally:
        db.close()

def obtener_estudiante_por_id(id_estudiante: UUID) -> Optional[Estudiante]:
    db = SessionLocal()
    try:
        return (
            db.query(Estudiante)
            .filter(Estudiante.id_estudiante == id_estudiante)
            .first()
        )
    finally:
        db.close()
