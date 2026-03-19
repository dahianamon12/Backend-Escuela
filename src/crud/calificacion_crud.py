from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal

from src.entities.calificacion import Calificacion

def crear_calificacion(
    nota: str, id_estudiante: UUID, id_curso: UUID, id_usuario_creacion: UUID
) -> Calificacion:
    db = SessionLocal()
    try:
        calificacion = Calificacion(
            nota=nota,
            id_estudiante=id_estudiante,
            id_curso=id_curso,
            id_usuario_creacion=id_usuario_creacion,
        )
        db.add(calificacion)
        db.commit()
        db.refresh(calificacion)
        return calificacion
    finally:
        db.close()

def obtener_calificaciones_por_estudiante(id_estudiante: UUID) -> List[Calificacion]:
    db = SessionLocal()
    try:
        return (
            db.query(Calificacion)
            .filter(Calificacion.id_estudiante == id_estudiante)
            .all()
        )
    finally:
        db.close()

def actualizar_calificacion(
    id_calificacion: UUID, id_usuario_edita: UUID, **kwargs
) -> Optional[Calificacion]:
    db = SessionLocal()
    try:

        calificacion = (
            db.query(Calificacion)
            .filter(Calificacion.id_calificacion == id_calificacion)
            .first()
        )
        if not calificacion:
            return None
        for key, value in kwargs.items():
            if hasattr(calificacion, key) and value is not None:
                setattr(calificacion, key, value)
        calificacion.id_usuario_edita = id_usuario_edita
        db.commit()
        db.refresh(calificacion)
        return calificacion
    finally:
        db.close()