from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.crud import departamento_crud
from src.database.config import SessionLocal
from src.entities.departamento import Departamento

router = APIRouter(prefix="/departamentos", tags=["Departamentos"])


class DepartamentoCreate(BaseModel):
    nombre: str
    telefono: str
    oficina: str
    id_usuario_creacion: UUID


class DepartamentoUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    oficina: Optional[str] = None
    id_usuario_edita: UUID


class DepartamentoResponse(BaseModel):
    id_departamento: UUID
    nombre: str
    telefono: Optional[str] = None
    oficina: Optional[str] = None

    model_config = {"from_attributes": True}


@router.get("/", response_model=List[DepartamentoResponse])
def listar_departamentos():
    db = SessionLocal()
    try:
        return db.query(Departamento).all()
    finally:
        db.close()


@router.get("/{id_departamento}", response_model=DepartamentoResponse)
def obtener_departamento(id_departamento: UUID):
    db = SessionLocal()
    try:
        depto = (
            db.query(Departamento)
            .filter(Departamento.id_departamento == id_departamento)
            .first()
        )
        if not depto:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        return depto
    finally:
        db.close()


@router.post("/", response_model=DepartamentoResponse, status_code=201)
def crear_departamento(data: DepartamentoCreate):
    return departamento_crud.crear_departamento(
        data.nombre, data.telefono, data.oficina, data.id_usuario_creacion
    )


@router.put("/{id_departamento}", response_model=DepartamentoResponse)
def actualizar_departamento(id_departamento: UUID, data: DepartamentoUpdate):
    db = SessionLocal()
    try:
        depto = (
            db.query(Departamento)
            .filter(Departamento.id_departamento == id_departamento)
            .first()
        )
        if not depto:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        if data.nombre is not None:
            depto.nombre = data.nombre
        if data.telefono is not None:
            depto.telefono = data.telefono
        if data.oficina is not None:
            depto.oficina = data.oficina
        depto.id_usuario_edita = data.id_usuario_edita
        db.commit()
        db.refresh(depto)
        return depto
    finally:
        db.close()


@router.delete("/{id_departamento}", status_code=204)
def eliminar_departamento(id_departamento: UUID):
    db = SessionLocal()
    try:
        depto = (
            db.query(Departamento)
            .filter(Departamento.id_departamento == id_departamento)
            .first()
        )
        if not depto:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        db.delete(depto)
        db.commit()
    finally:
        db.close()
