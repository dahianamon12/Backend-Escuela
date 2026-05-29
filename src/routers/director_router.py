from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.crud import director_crud
from src.database.config import SessionLocal
from src.entities.director import Director

router = APIRouter(prefix="/directores", tags=["Directores"])


class DirectorCreate(BaseModel):
    id_usuario: UUID
    id_departamento: UUID
    telefono: str
    id_usuario_creacion: UUID


class DirectorUpdate(BaseModel):
    id_departamento: Optional[UUID] = None
    telefono: Optional[str] = None
    id_usuario_edita: UUID


class DirectorResponse(BaseModel):
    id_director: UUID
    id_departamento: Optional[UUID] = None
    telefono: Optional[str] = None

    model_config = {"from_attributes": True}


@router.get("/", response_model=List[DirectorResponse])
def listar_directores():
    db = SessionLocal()
    try:
        return db.query(Director).all()
    finally:
        db.close()


@router.get("/{id_director}", response_model=DirectorResponse)
def obtener_director(id_director: UUID):
    db = SessionLocal()
    try:
        director = db.query(Director).filter(Director.id_director == id_director).first()
        if not director:
            raise HTTPException(status_code=404, detail="Director no encontrado")
        return director
    finally:
        db.close()


@router.post("/", response_model=DirectorResponse, status_code=201)
def crear_director(data: DirectorCreate):
    return director_crud.crear_director(
        data.id_usuario, data.id_departamento, data.telefono, data.id_usuario_creacion
    )


@router.put("/{id_director}", response_model=DirectorResponse)
def actualizar_director(id_director: UUID, data: DirectorUpdate):
    db = SessionLocal()
    try:
        director = db.query(Director).filter(Director.id_director == id_director).first()
        if not director:
            raise HTTPException(status_code=404, detail="Director no encontrado")
        if data.id_departamento is not None:
            director.id_departamento = data.id_departamento
        if data.telefono is not None:
            director.telefono = data.telefono
        director.id_usuario_edita = data.id_usuario_edita
        db.commit()
        db.refresh(director)
        return director
    finally:
        db.close()


@router.delete("/{id_director}", status_code=204)
def eliminar_director(id_director: UUID):
    db = SessionLocal()
    try:
        director = db.query(Director).filter(Director.id_director == id_director).first()
        if not director:
            raise HTTPException(status_code=404, detail="Director no encontrado")
        db.delete(director)
        db.commit()
    finally:
        db.close()