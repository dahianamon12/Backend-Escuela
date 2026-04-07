from typing import List, Optional
from uuid import UUID
from datetime import datetime

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.crud import estudiante_crud
from src.database.config import SessionLocal
from src.entities.estudiante import Estudiante

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])


class EstudianteCreate(BaseModel):
    id_usuario: UUID
    id_grado: UUID
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[datetime] = None
    id_usuario_creacion: UUID


class EstudianteUpdate(BaseModel):
    id_grado: Optional[UUID] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[datetime] = None
    id_usuario_edita: UUID


class EstudianteResponse(BaseModel):
    id_estudiante: UUID
    id_grado: Optional[UUID] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    fecha_nacimiento: Optional[datetime] = None

    model_config = {"from_attributes": True}


@router.get("/", response_model=List[EstudianteResponse])
def listar_estudiantes():
    db = SessionLocal()
    try:
        return db.query(Estudiante).all()
    finally:
        db.close()


@router.get("/{id_estudiante}", response_model=EstudianteResponse)
def obtener_estudiante(id_estudiante: UUID):
    estudiante = estudiante_crud.obtener_estudiante_por_id(id_estudiante)
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return estudiante


@router.post("/", response_model=EstudianteResponse, status_code=201)
def crear_estudiante(data: EstudianteCreate):
    return estudiante_crud.crear_estudiante(
        data.id_usuario,
        data.id_grado,
        data.id_usuario_creacion,
        direccion=data.direccion,
        telefono=data.telefono,
        fecha_nacimiento=data.fecha_nacimiento,
    )


@router.put("/{id_estudiante}", response_model=EstudianteResponse)
def actualizar_estudiante(id_estudiante: UUID, data: EstudianteUpdate):
    db = SessionLocal()
    try:
        est = (
            db.query(Estudiante)
            .filter(Estudiante.id_estudiante == id_estudiante)
            .first()
        )
        if not est:
            raise HTTPException(status_code=404, detail="Estudiante no encontrado")
        if data.id_grado is not None:
            est.id_grado = data.id_grado
        if data.direccion is not None:
            est.direccion = data.direccion
        if data.telefono is not None:
            est.telefono = data.telefono
        if data.fecha_nacimiento is not None:
            est.fecha_nacimiento = data.fecha_nacimiento
        est.id_usuario_edita = data.id_usuario_edita
        db.commit()
        db.refresh(est)
        return est
    finally:
        db.close()


@router.delete("/{id_estudiante}", status_code=204)
def eliminar_estudiante(id_estudiante: UUID):
    db = SessionLocal()
    try:
        est = (
            db.query(Estudiante)
            .filter(Estudiante.id_estudiante == id_estudiante)
            .first()
        )
        if not est:
            raise HTTPException(status_code=404, detail="Estudiante no encontrado")
        db.delete(est)
        db.commit()
    finally:
        db.close()
