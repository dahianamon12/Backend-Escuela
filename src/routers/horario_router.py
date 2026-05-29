from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.crud import horario_crud
from src.database.config import SessionLocal
from src.entities.horario import Horario

router = APIRouter(prefix="/horarios", tags=["Horarios"])


class HorarioCreate(BaseModel):
    dia: str
    hora_inicio: str
    hora_fin: str
    id_curso: UUID
    id_usuario_creacion: UUID


class HorarioUpdate(BaseModel):
    dia: Optional[str] = None
    hora_inicio: Optional[str] = None
    hora_fin: Optional[str] = None
    id_curso: Optional[UUID] = None
    id_usuario_edita: UUID


class HorarioResponse(BaseModel):
    id_horario: UUID
    dia: Optional[str] = None
    hora_inicio: Optional[str] = None
    hora_fin: Optional[str] = None
    id_curso: Optional[UUID] = None

    model_config = {"from_attributes": True}


@router.get("/", response_model=List[HorarioResponse])
def listar_horarios():
    db = SessionLocal()
    try:
        return db.query(Horario).all()
    finally:
        db.close()


@router.get("/{id_horario}", response_model=HorarioResponse)
def obtener_horario(id_horario: UUID):
    db = SessionLocal()
    try:
        horario = db.query(Horario).filter(Horario.id_horario == id_horario).first()
        if not horario:
            raise HTTPException(status_code=404, detail="Horario no encontrado")
        return horario
    finally:
        db.close()


@router.post("/", response_model=HorarioResponse, status_code=201)
def crear_horario(data: HorarioCreate):
    return horario_crud.crear_horario(
        data.dia, data.hora_inicio, data.hora_fin,
        data.id_curso, data.id_usuario_creacion
    )


@router.put("/{id_horario}", response_model=HorarioResponse)
def actualizar_horario(id_horario: UUID, data: HorarioUpdate):
    db = SessionLocal()
    try:
        horario = db.query(Horario).filter(Horario.id_horario == id_horario).first()
        if not horario:
            raise HTTPException(status_code=404, detail="Horario no encontrado")
        if data.dia is not None:
            horario.dia = data.dia
        if data.hora_inicio is not None:
            horario.hora_inicio = data.hora_inicio
        if data.hora_fin is not None:
            horario.hora_fin = data.hora_fin
        if data.id_curso is not None:
            horario.id_curso = data.id_curso
        horario.id_usuario_edita = data.id_usuario_edita
        db.commit()
        db.refresh(horario)
        return horario
    finally:
        db.close()


@router.delete("/{id_horario}", status_code=204)
def eliminar_horario(id_horario: UUID):
    db = SessionLocal()
    try:
        horario = db.query(Horario).filter(Horario.id_horario == id_horario).first()
        if not horario:
            raise HTTPException(status_code=404, detail="Horario no encontrado")
        db.delete(horario)
        db.commit()
    finally:
        db.close()