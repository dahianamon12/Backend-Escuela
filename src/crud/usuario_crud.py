import hashlib
from typing import List, Optional
from uuid import UUID

from src.database.config import SessionLocal
from src.entities.usuario import Usuario

db = SessionLocal()


def _hash_contrasena(contrasena: str) -> str:
    """Hashea la contraseña con SHA-256 (para no guardar en claro)."""
    return hashlib.sha256(contrasena.encode("utf-8")).hexdigest()


def crear(
    nombre: str,
    email: str,
    nombre_usuario: str,
    contrasena: str,
    rol: str = "usuario",
    activo: bool = True,
) -> Usuario:

    db = SessionLocal()
    try:
        usuario_existente = (
            db.query(Usuario)
            .filter(
                (Usuario.nombre_usuario == nombre_usuario.strip())
                | (Usuario.email == email.strip())
            )
            .first()
        )
        if usuario_existente:
            raise ValueError("El nombre de usuario o el email ya están registrados")

        usuario = Usuario(
            nombre=nombre.strip(),
            email=email.strip().lower(),
            nombre_usuario=nombre_usuario.strip(),
            contrasena=_hash_contrasena(contrasena),
            rol=rol.strip(),
            activo=activo,
        )

        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    finally:
        db.close()


def login(nombre_usuario: str, contrasena: str) -> Optional[Usuario]:
    db = SessionLocal()
    try:
        usuario = (
            db.query(Usuario)
            .filter(Usuario.nombre_usuario == nombre_usuario.strip())
            .first()
        )
        if not usuario or not usuario.activo:
            return None
        if usuario.contrasena != _hash_contrasena(contrasena):
            return None
        return usuario
    finally:
        db.close()



def obtener_por_id(id_usuario: UUID) -> Optional[Usuario]:
    db = SessionLocal()
    try:
        return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    finally:
        db.close()


def obtener_por_nombre_usuario(nombre_usuario: str) -> Optional[Usuario]:
    db = SessionLocal()
    try:
        return (
            db.query(Usuario)
            .filter(Usuario.nombre_usuario == nombre_usuario.strip())
            .first()
        )
    finally:
        db.close()


def obtener_todos() -> List[Usuario]:
    db = SessionLocal()
    try:
        return db.query(Usuario).all()
    finally:
        db.close()


def hay_usuarios() -> bool:
    db = SessionLocal()
    try:
        return db.query(Usuario).first() is not None
    finally:
        db.close()


def actualizar(
    id_usuario: UUID,
    *,
    nombre: Optional[str] = None,
    email: Optional[str] = None,
    nombre_usuario: Optional[str] = None,
    contrasena: Optional[str] = None,
    rol: Optional[str] = None,
    activo: Optional[bool] = None,
) -> Optional[Usuario]:
    db = SessionLocal()
    try:
        usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if not usuario:
            return None
        if nombre is not None:
            usuario.nombre = nombre.strip()
        if email is not None:
            usuario.email = email.strip().lower()
        if nombre_usuario is not None:
            usuario.nombre_usuario = nombre_usuario.strip()
        if contrasena is not None:
            usuario.contrasena = _hash_contrasena(contrasena)
        if rol is not None:
            usuario.rol = rol.strip()
        if activo is not None:
            usuario.activo = activo
        db.commit()
        db.refresh(usuario)
        return usuario
    finally:
        db.close()


def eliminar(id_usuario: UUID) -> bool:
    db = SessionLocal()
    try:
        usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if not usuario:
            return False
        db.delete(usuario)
        db.commit()
        return True
    finally:
        db.close()