from typing import Optional
from uuid import UUID

from src.database.config import SessionLocal

from entities.aula import Aula

db = SessionLocal()


def crear_aula(
    numero_aula: str, capacidad: str, edificio: str, id_usuario_creacion: UUID
) -> Aula:
    aula = Aula(
        numero_aula=numero_aula,
        capacidad=capacidad,
        edificio=edificio,
        id_usuario_creacion=id_usuario_creacion,
    )
    db.add(aula)
    db.commit()
    db.refresh(aula)
    return aula


def actualizar_aula(id_aula: UUID, id_usuario_edita: UUID, **kwargs) -> Optional[Aula]:
    aula = db.query(Aula).filter(Aula.id_aula == id_aula).first()
    if not aula:
        return None
    for key, value in kwargs.items():
        if hasattr(aula, key) and value is not None:
            setattr(aula, key, value)
    aula.id_usuario_edita = id_usuario_edita
    db.commit()
    db.refresh(aula)
    return aula
