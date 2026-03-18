from uuid import UUID

from src.database.config import SessionLocal

from entities.director import Director

db = SessionLocal()


def crear_director(
    id_usuario: UUID, id_departamento: UUID, telefono: str, id_usuario_creacion: UUID
) -> Director:
    director = Director(
        id_director=id_usuario,
        id_departamento=id_departamento,
        telefono=telefono,
        id_usuario_creacion=id_usuario_creacion,
    )
    db.add(director)
    db.commit()
    db.refresh(director)
    return director
