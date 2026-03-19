from typing import Optional
from uuid import UUID

from src.database.config import SessionLocal

from src.entities.grado import Grado

def crear_grado(
    nombre_grado: str, nivel: str, jornada: str, id_usuario_creacion: UUID
) -> Grado:
    db = SessionLocal()
    try:
        grado = Grado(
            nombre_grado=nombre_grado,
            nivel=nivel,
            jornada=jornada,
            id_usuario_creacion=id_usuario_creacion,
        )
        db.add(grado)
        db.commit()
        db.refresh(grado)
        return grado
    finally:
        db.close()

def obtener_grado_por_id(id_grado: UUID) -> Optional[Grado]:
    db = SessionLocal()
    try:
        return db.query(Grado).filter(Grado.id_grado == id_grado).first()
    finally:
        db.close()

def actualizar_grado(
    id_grado: UUID, id_usuario_edita: UUID, **kwargs
) -> Optional[Grado]:
    db = SessionLocal()
    try:
        grado = obtener_grado_por_id(id_grado)
        if not grado:
            return None
        for key, value in kwargs.items():
            if hasattr(grado, key) and value is not None:
                setattr(grado, key, value)
        grado.id_usuario_edita = id_usuario_edita
        db.commit()
        db.refresh(grado)
        return grado
    finally:
        db.close()