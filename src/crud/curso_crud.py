from typing import List
from uuid import UUID

from src.database.config import SessionLocal

from entities.curso import Curso

db = SessionLocal()


def crear_curso(
    nombre_curso: str,
    id_profesor: UUID,
    id_grado: UUID,
    id_aula: UUID,
    id_usuario_creacion: UUID,
    **kwargs
) -> Curso:
    curso = Curso(
        nombre_curso=nombre_curso,
        id_profesor=id_profesor,
        id_grado=id_grado,
        id_aula=id_aula,
        id_usuario_creacion=id_usuario_creacion,
        **kwargs
    )
    db.add(curso)
    db.commit()
    db.refresh(curso)
    return curso


def obtener_cursos_por_grado(id_grado: UUID) -> List[Curso]:
    return db.query(Curso).filter(Curso.id_grado == id_grado).all()
