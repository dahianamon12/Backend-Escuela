from uuid import UUID

from src.database.config import SessionLocal

from entities.departamento import Departamento

db = SessionLocal()


def crear_departamento(
    nombre: str, telefono: str, oficina: str, id_usuario_creacion: UUID
) -> Departamento:
    depto = Departamento(
        nombre=nombre,
        telefono=telefono,
        oficina=oficina,
        id_usuario_creacion=id_usuario_creacion,
    )
    db.add(depto)
    db.commit()
    db.refresh(depto)
    return depto
