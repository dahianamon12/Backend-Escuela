from uuid import UUID

from src.database.config import SessionLocal

from src.entities.profesor import Profesor

def crear_profesor(
    id_usuario: UUID,
    id_departamento: UUID,
    especialidad: str,
    id_usuario_creacion: UUID,
) -> Profesor:
    db = SessionLocal()
    try:
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
    finally:
        db.close()