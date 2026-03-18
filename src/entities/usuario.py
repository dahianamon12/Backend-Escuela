import uuid
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field
from src.database.config import Base


class Usuario(Base):

    __tablename__ = "usuario"

    id_usuario = Column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )

    nombre = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False, unique=True)

    nombre_usuario = Column(String(150), nullable=False, unique=True)
    contrasena = Column(String(255), nullable=False)
    rol = Column(String(50), nullable=False)
    activo = Column(Boolean, default=True)

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())


class PersonaBase(BaseModel):

    nombre: str = Field(..., min_length=1, max_length=150)
    email: EmailStr
    nombre_usuario: str = Field(..., min_length=3, max_length=150)
    rol: str
    activo: bool = True


class PersonaCreate(PersonaBase):
    contrasena: str = Field(..., min_length=8)


class PersonaUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=150)
    email: Optional[EmailStr] = None
    nombre_usuario: Optional[str] = Field(None, min_length=3, max_length=150)
    rol: Optional[str] = None
    activo: Optional[bool] = None
    contrasena: Optional[str] = Field(None, min_length=8)

    class Config:
        from_attributes = True


class PersonaResponse(PersonaBase):

    id_usuario: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None

    class Config:
        from_attributes = True
