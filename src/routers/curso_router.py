from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.crud import curso_crud
from src.database.config import SessionLocal
from src.entities.curso import Curso

router = APIRouter(prefix="/cursos", tags=["Cursos"])


class CursoCreate(BaseModel):
    nombre_curso: str
    descripcion: Optional[str] = None
    horas_semanales: Optional[str] = None
    id_profesor: UUID
    id_grado: UUID
    id_aula: UUID
    id_usuario_creacion: UUID


class CursoUpdate(BaseModel):
    nombre_curso: Optional[str] = None
    descripcion: Optional[str] = None
    horas_semanales: Optional[str] = None
    id_profesor: Optional[UUID] = None
    id_grado: Optional[UUID] = None
    id_aula: Optional[UUID] = None
    id_usuario_edita: UUID


class CursoResponse(BaseModel):
    id_curso: UUID
    nombre_curso: str
    descripcion: Optional[str] = None
    horas_semanales: Optional[str] = None
    id_profesor: Optional[UUID] = None
    id_grado: Optional[UUID] = None
    id_aula: Optional[UUID] = None

    model_config = {"from_attributes": True}


@router.get("/", response_model=List[CursoResponse])
def listar_cursos():
    db = SessionLocal()
    try:
        return db.query(Curso).all()
    finally:
        db.close()


@router.get("/{id_curso}", response_model=CursoResponse)
def obtener_curso(id_curso: UUID):
    db = SessionLocal()
    try:
        curso = db.query(Curso).filter(Curso.id_curso == id_curso).first()
        if not curso:
            raise HTTPException(status_code=404, detail="Curso no encontrado")
        return curso
    finally:
        db.close()


@router.post("/", response_model=CursoResponse, status_code=201)
def crear_curso(data: CursoCreate):
    return curso_crud.crear_curso(
        data.nombre_curso, data.id_profesor, data.id_grado,
        data.id_aula, data.id_usuario_creacion,
        descripcion=data.descripcion,
        horas_semanales=data.horas_semanales,
    )


@router.put("/{id_curso}", response_model=CursoResponse)
def actualizar_curso(id_curso: UUID, data: CursoUpdate):
    db = SessionLocal()
    try:
        curso = db.query(Curso).filter(Curso.id_curso == id_curso).first()
        if not curso:
            raise HTTPException(status_code=404, detail="Curso no encontrado")
        if data.nombre_curso is not None:
            curso.nombre_curso = data.nombre_curso
        if data.descripcion is not None:
            curso.descripcion = data.descripcion
        if data.horas_semanales is not None:
            curso.horas_semanales = data.horas_semanales
        if data.id_profesor is not None:
            curso.id_profesor = data.id_profesor
        if data.id_grado is not None:
            curso.id_grado = data.id_grado
        if data.id_aula is not None:
            curso.id_aula = data.id_aula
        curso.id_usuario_edita = data.id_usuario_edita
        db.commit()
        db.refresh(curso)
        return curso
    finally:
        db.close()


@router.delete("/{id_curso}", status_code=204)
def eliminar_curso(id_curso: UUID):
    db = SessionLocal()
    try:
        curso = db.query(Curso).filter(Curso.id_curso == id_curso).first()
        if not curso:
            raise HTTPException(status_code=404, detail="Curso no encontrado")
        db.delete(curso)
        db.commit()
    finally:
        db.close()