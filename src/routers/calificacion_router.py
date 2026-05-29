from typing import List, Optional
from uuid import UUID
from datetime import datetime

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.crud import calificacion_crud
from src.database.config import SessionLocal
from src.entities.calificacion import Calificacion

router = APIRouter(prefix="/calificaciones", tags=["Calificaciones"])


class CalificacionCreate(BaseModel):
    nota: str
    id_estudiante: UUID
    id_curso: UUID
    id_usuario_creacion: UUID


class CalificacionUpdate(BaseModel):
    nota: Optional[str] = None
    id_usuario_edita: UUID


class CalificacionResponse(BaseModel):
    id_calificacion: UUID
    nota: Optional[str] = None
    id_estudiante: Optional[UUID] = None
    id_curso: Optional[UUID] = None

    model_config = {"from_attributes": True}


@router.get("/", response_model=List[CalificacionResponse])
def listar_calificaciones():
    db = SessionLocal()
    try:
        return db.query(Calificacion).all()
    finally:
        db.close()


@router.get("/{id_calificacion}", response_model=CalificacionResponse)
def obtener_calificacion(id_calificacion: UUID):
    db = SessionLocal()
    try:
        cal = db.query(Calificacion).filter(
            Calificacion.id_calificacion == id_calificacion
        ).first()
        if not cal:
            raise HTTPException(status_code=404, detail="Calificación no encontrada")
        return cal
    finally:
        db.close()


@router.post("/", response_model=CalificacionResponse, status_code=201)
def crear_calificacion(data: CalificacionCreate):
    return calificacion_crud.crear_calificacion(
        data.nota, data.id_estudiante, data.id_curso, data.id_usuario_creacion
    )


@router.put("/{id_calificacion}", response_model=CalificacionResponse)
def actualizar_calificacion(id_calificacion: UUID, data: CalificacionUpdate):
    cal = calificacion_crud.actualizar_calificacion(
        id_calificacion, data.id_usuario_edita, nota=data.nota
    )
    if not cal:
        raise HTTPException(status_code=404, detail="Calificación no encontrada")
    return cal


@router.delete("/{id_calificacion}", status_code=204)
def eliminar_calificacion(id_calificacion: UUID):
    db = SessionLocal()
    try:
        cal = db.query(Calificacion).filter(
            Calificacion.id_calificacion == id_calificacion
        ).first()
        if not cal:
            raise HTTPException(status_code=404, detail="Calificación no encontrada")
        db.delete(cal)
        db.commit()
    finally:
        db.close()