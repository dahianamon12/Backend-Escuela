from uuid import UUID

from src.database.config import SessionLocal

from entities.horario import Horario

db = SessionLocal()


def crear_horario(
    dia: str, hora_inicio: str, hora_fin: str, id_curso: UUID, id_usuario_creacion: UUID
) -> Horario:
    horario = Horario(
        dia=dia,
        hora_inicio=hora_inicio,
        hora_fin=hora_fin,
        id_curso=id_curso,
        id_usuario_creacion=id_usuario_creacion,
    )
    db.add(horario)
    db.commit()
    db.refresh(horario)
    return horario
