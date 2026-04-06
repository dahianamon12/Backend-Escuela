from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional

from src.crud import usuario_crud

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    nombre_usuario: str
    contrasena: str
    rol: str = "usuario"
    activo: bool = True


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None
    nombre_usuario: Optional[str] = None
    contrasena: Optional[str] = None
    rol: Optional[str] = None
    activo: Optional[bool] = None


class UsuarioResponse(BaseModel):
    id_usuario: UUID
    nombre: str
    email: str
    nombre_usuario: str
    rol: str
    activo: bool

    model_config = {"from_attributes": True}


@router.get("/", response_model=List[UsuarioResponse])
def listar_usuarios():
    return usuario_crud.obtener_todos()


@router.get("/{id_usuario}", response_model=UsuarioResponse)
def obtener_usuario(id_usuario: UUID):
    usuario = usuario_crud.obtener_por_id(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.post("/", response_model=UsuarioResponse, status_code=201)
def crear_usuario(data: UsuarioCreate):
    try:
        return usuario_crud.crear(
            data.nombre, data.email, data.nombre_usuario,
            data.contrasena, data.rol, data.activo
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{id_usuario}", response_model=UsuarioResponse)
def actualizar_usuario(id_usuario: UUID, data: UsuarioUpdate):
    usuario = usuario_crud.actualizar(
        id_usuario,
        nombre=data.nombre,
        email=data.email,
        nombre_usuario=data.nombre_usuario,
        contrasena=data.contrasena,
        rol=data.rol,
        activo=data.activo,
    )
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.delete("/{id_usuario}", status_code=204)
def eliminar_usuario(id_usuario: UUID):
    eliminado = usuario_crud.eliminar(id_usuario)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")