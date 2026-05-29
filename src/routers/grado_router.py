from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.crud import grado_crud
from src.database.config import SessionLocal
from src.entities.grado import Grado

router = APIRouter(prefix="/grados", tags=["Grados"])


class GradoCreate(BaseModel):
    nombre_grado: str
    nivel: str
    jornada: str
    id_usuario_creacion: UUID


class GradoUpdate(BaseModel):
    nombre_grado: Optional[str] = None
    nivel: Optional[str] = None
    jornada: Optional[str] = None
    id_usuario_edita: UUID


class GradoResponse(BaseModel):
    id_grado: UUID
    nombre_grado: str
    nivel: Optional[str] = None
    jornada: Optional[str] = None

    model_config = {"from_attributes": True}


@router.get("/", response_model=List[GradoResponse])
def listar_grados():
    db = SessionLocal()
    try:
        return db.query(Grado).all()
    finally:
        db.close()


@router.get("/{id_grado}", response_model=GradoResponse)
def obtener_grado(id_grado: UUID):
    grado = grado_crud.obtener_grado_por_id(id_grado)
    if not grado:
        raise HTTPException(status_code=404, detail="Grado no encontrado")
    return grado


@router.post("/", response_model=GradoResponse, status_code=201)
def crear_grado(data: GradoCreate):
    return grado_crud.crear_grado(
        data.nombre_grado, data.nivel, data.jornada, data.id_usuario_creacion
    )


@router.put("/{id_grado}", response_model=GradoResponse)
def actualizar_grado(id_grado: UUID, data: GradoUpdate):
    grado = grado_crud.actualizar_grado(
        id_grado,
        data.id_usuario_edita,
        nombre_grado=data.nombre_grado,
        nivel=data.nivel,
        jornada=data.jornada,
    )
    if not grado:
        raise HTTPException(status_code=404, detail="Grado no encontrado")
    return grado


@router.delete("/{id_grado}", status_code=204)
def eliminar_grado(id_grado: UUID):
    db = SessionLocal()
    try:
        grado = db.query(Grado).filter(Grado.id_grado == id_grado).first()
        if not grado:
            raise HTTPException(status_code=404, detail="Grado no encontrado")
        db.delete(grado)
        db.commit()
    finally:
        db.close()