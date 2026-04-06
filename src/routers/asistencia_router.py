from typing import List, Optional
from uuid import UUID
from datetime import datetime

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.crud import asistencia_crud
from src.database.config import SessionLocal
from src.entities.asistencia import Asistencia

router = APIRouter(prefix="/asistencias", tags=["Asistencias"])


class AsistenciaCreate(BaseModel):
    fecha: datetime
    estado: str
    id_estudiante: UUID
    id_curso: UUID
    id_usuario_creacion: UUID


class AsistenciaUpdate(BaseModel):
    fecha: Optional[datetime] = None
    estado: Optional[str] = None
    id_usuario_edita: UUID


class AsistenciaResponse(BaseModel):
    id_asistencia: UUID
    fecha: Optional[datetime] = None
    estado: Optional[str] = None
    id_estudiante: Optional[UUID] = None
    id_curso: Optional[UUID] = None

    model_config = {"from_attributes": True}


@router.get("/", response_model=List[AsistenciaResponse])
def listar_asistencias():
    db = SessionLocal()
    try:
        return db.query(Asistencia).all()
    finally:
        db.close()


@router.get("/{id_asistencia}", response_model=AsistenciaResponse)
def obtener_asistencia(id_asistencia: UUID):
    db = SessionLocal()
    try:
        asis = db.query(Asistencia).filter(
            Asistencia.id_asistencia == id_asistencia
        ).first()
        if not asis:
            raise HTTPException(status_code=404, detail="Asistencia no encontrada")
        return asis
    finally:
        db.close()


@router.post("/", response_model=AsistenciaResponse, status_code=201)
def crear_asistencia(data: AsistenciaCreate):
    return asistencia_crud.crear_asistencia(
        data.fecha, data.estado, data.id_estudiante,
        data.id_curso, data.id_usuario_creacion
    )


@router.put("/{id_asistencia}", response_model=AsistenciaResponse)
def actualizar_asistencia(id_asistencia: UUID, data: AsistenciaUpdate):
    db = SessionLocal()
    try:
        asis = db.query(Asistencia).filter(
            Asistencia.id_asistencia == id_asistencia
        ).first()
        if not asis:
            raise HTTPException(status_code=404, detail="Asistencia no encontrada")
        if data.fecha is not None:
            asis.fecha = data.fecha
        if data.estado is not None:
            asis.estado = data.estado
        asis.id_usuario_edita = data.id_usuario_edita
        db.commit()
        db.refresh(asis)
        return asis
    finally:
        db.close()


@router.delete("/{id_asistencia}", status_code=204)
def eliminar_asistencia(id_asistencia: UUID):
    db = SessionLocal()
    try:
        asis = db.query(Asistencia).filter(
            Asistencia.id_asistencia == id_asistencia
        ).first()
        if not asis:
            raise HTTPException(status_code=404, detail="Asistencia no encontrada")
        db.delete(asis)
        db.commit()
    finally:
        db.close()