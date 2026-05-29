from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.crud import profesor_crud
from src.database.config import SessionLocal
from src.entities.profesor import Profesor

router = APIRouter(prefix="/profesores", tags=["Profesores"])


class ProfesorCreate(BaseModel):
    id_usuario: UUID
    id_departamento: UUID
    especialidad: str
    id_usuario_creacion: UUID


class ProfesorUpdate(BaseModel):
    id_departamento: Optional[UUID] = None
    especialidad: Optional[str] = None
    id_usuario_edita: UUID


class ProfesorResponse(BaseModel):
    id_profesor: UUID
    id_departamento: Optional[UUID] = None
    especialidad: Optional[str] = None

    model_config = {"from_attributes": True}


@router.get("/", response_model=List[ProfesorResponse])
def listar_profesores():
    db = SessionLocal()
    try:
        return db.query(Profesor).all()
    finally:
        db.close()


@router.get("/{id_profesor}", response_model=ProfesorResponse)
def obtener_profesor(id_profesor: UUID):
    db = SessionLocal()
    try:
        profesor = (
            db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()
        )
        if not profesor:
            raise HTTPException(status_code=404, detail="Profesor no encontrado")
        return profesor
    finally:
        db.close()


@router.post("/", response_model=ProfesorResponse, status_code=201)
def crear_profesor(data: ProfesorCreate):
    return profesor_crud.crear_profesor(
        data.id_usuario,
        data.id_departamento,
        data.especialidad,
        data.id_usuario_creacion,
    )


@router.put("/{id_profesor}", response_model=ProfesorResponse)
def actualizar_profesor(id_profesor: UUID, data: ProfesorUpdate):
    db = SessionLocal()
    try:
        prof = db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()
        if not prof:
            raise HTTPException(status_code=404, detail="Profesor no encontrado")
        if data.id_departamento is not None:
            prof.id_departamento = data.id_departamento
        if data.especialidad is not None:
            prof.especialidad = data.especialidad
        prof.id_usuario_edita = data.id_usuario_edita
        db.commit()
        db.refresh(prof)
        return prof
    finally:
        db.close()


@router.delete("/{id_profesor}", status_code=204)
def eliminar_profesor(id_profesor: UUID):
    db = SessionLocal()
    try:
        prof = db.query(Profesor).filter(Profesor.id_profesor == id_profesor).first()
        if not prof:
            raise HTTPException(status_code=404, detail="Profesor no encontrado")
        db.delete(prof)
        db.commit()
    finally:
        db.close()