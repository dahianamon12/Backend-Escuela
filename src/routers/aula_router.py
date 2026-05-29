from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.crud import aula_crud
from src.database.config import SessionLocal
from src.entities.aula import Aula

router = APIRouter(prefix="/aulas", tags=["Aulas"])


class AulaCreate(BaseModel):
    numero_aula: str
    capacidad: str
    edificio: str
    id_usuario_creacion: UUID


class AulaUpdate(BaseModel):
    numero_aula: Optional[str] = None
    capacidad: Optional[str] = None
    edificio: Optional[str] = None
    id_usuario_edita: UUID


class AulaResponse(BaseModel):
    id_aula: UUID
    numero_aula: str
    capacidad: Optional[str] = None
    edificio: Optional[str] = None

    model_config = {"from_attributes": True}


@router.get("/", response_model=List[AulaResponse])
def listar_aulas():
    db = SessionLocal()
    try:
        return db.query(Aula).all()
    finally:
        db.close()


@router.get("/{id_aula}", response_model=AulaResponse)
def obtener_aula(id_aula: UUID):
    db = SessionLocal()
    try:
        aula = db.query(Aula).filter(Aula.id_aula == id_aula).first()
        if not aula:
            raise HTTPException(status_code=404, detail="Aula no encontrada")
        return aula
    finally:
        db.close()


@router.post("/", response_model=AulaResponse, status_code=201)
def crear_aula(data: AulaCreate):
    return aula_crud.crear_aula(
        data.numero_aula, data.capacidad, data.edificio, data.id_usuario_creacion
    )


@router.put("/{id_aula}", response_model=AulaResponse)
def actualizar_aula(id_aula: UUID, data: AulaUpdate):
    aula = aula_crud.actualizar_aula(
        id_aula,
        data.id_usuario_edita,
        numero_aula=data.numero_aula,
        capacidad=data.capacidad,
        edificio=data.edificio,
    )
    if not aula:
        raise HTTPException(status_code=404, detail="Aula no encontrada")
    return aula


@router.delete("/{id_aula}", status_code=204)
def eliminar_aula(id_aula: UUID):
    db = SessionLocal()
    try:
        aula = db.query(Aula).filter(Aula.id_aula == id_aula).first()
        if not aula:
            raise HTTPException(status_code=404, detail="Aula no encontrada")
        db.delete(aula)
        db.commit()
    finally:
        db.close()
