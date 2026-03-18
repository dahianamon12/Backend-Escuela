from uuid import UUID

from src.database.config import SessionLocal

from entities.profesor import Profesor

db = SessionLocal()


def crear_profesor(
    id_usuario: UUID,
    id_departamento: UUID,
    especialidad: str,
    id_usuario_creacion: UUID,
) -> Profesor:
    profesor = Profesor(
        id_profesor=id_usuario,
        id_departamento=id_departamento,
        especialidad=especialidad,
        id_usuario_creacion=id_usuario_creacion,
    )
    db.add(profesor)
    db.commit()
    db.refresh(profesor)
    return profesor
