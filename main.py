import sys
from uuid import UUID
from typing import Optional

sys.path.insert(0, ".")
import src.entities
import datetime
from src.crud import usuario_crud
from src.crud import grado_crud
from src.crud import estudiante_crud
from src.crud import profesor_crud
from src.crud import curso_crud
from src.crud import calificacion_crud
from src.crud import aula_crud
from src.crud import asistencia_crud
from src.crud import departamento_crud

from src.entities.usuario import Usuario


def leer_texto(m: str) -> str:
    return input(m).strip()


def leer_uuid(m: str) -> Optional[UUID]:
    s = input(m).strip()
    if not s:
        return None
    try:
        return UUID(s)
    except ValueError:
        print(f"  [!] UUID inválido: '{s}'. Verifica que lo copiaste completo.")
        return None


def login_sistema() -> Optional[Usuario]:
    if not usuario_crud.hay_usuarios():
        print("\n[!] No hay usuarios. Cree el Administrador inicial.")
        nom = leer_texto("Nombre: ")
        em = leer_texto("Email: ")
        usr = leer_texto("Usuario: ")
        pw = leer_texto("Password: ")
        return usuario_crud.crear(nom, em, usr, pw, rol="ADMIN")

    while True:
        print("\n--- LOGIN ESCUELA ---")
        print("1. Iniciar Sesión")
        print("2. Crear nuevo usuario")
        op = leer_texto("Opción: ")

        if op == "1":
            u = leer_texto("Usuario: ")
            p = leer_texto("Password: ")
            user = usuario_crud.login(u, p)
            if user:
                return user
            print("Credenciales inválidas.")

        elif op == "2":
            nom = leer_texto("Nombre: ")
            em = leer_texto("Email: ")
            usr = leer_texto("Usuario: ")
            pw = leer_texto("Password: ")
            try:
                user = usuario_crud.crear(nom, em, usr, pw)
                print(f"Usuario creado exitosamente. Bienvenido {user.nombre}!")
                return user
            except ValueError as e:
                print(f"Error: {e}")


def mostrar_usuarios():
    usuarios = usuario_crud.obtener_todos()
    print("\n--- USUARIOS DISPONIBLES ---")
    for u in usuarios:
        print(f"  {u.nombre} | Usuario: {u.nombre_usuario} | ID: {u.id_usuario}")
    print()


def mostrar_grados():
    from src.crud import grado_crud
    from src.entities.grado import Grado
    from src.database.config import SessionLocal
    db = SessionLocal()
    try:
        grados = db.query(Grado).all()
        print("\n--- GRADOS DISPONIBLES ---")
        for g in grados:
            print(f"  {g.nombre_grado} | ID: {g.id_grado}")
        print()
    finally:
        db.close()


def mostrar_departamentos():
    from src.entities.departamento import Departamento
    from src.database.config import SessionLocal
    db = SessionLocal()
    try:
        deptos = db.query(Departamento).all()
        print("\n--- DEPARTAMENTOS DISPONIBLES ---")
        for d in deptos:
            print(f"  {d.nombre} | ID: {d.id_departamento}")
        print()
    finally:
        db.close()


def mostrar_cursos():
    from src.entities.curso import Curso
    from src.database.config import SessionLocal
    db = SessionLocal()
    try:
        cursos = db.query(Curso).all()
        print("\n--- CURSOS DISPONIBLES ---")
        for c in cursos:
            print(f"  {c.nombre_curso} | ID: {c.id_curso}")
        print()
    finally:
        db.close()


def mostrar_estudiantes():
    from src.entities.estudiante import Estudiante
    from src.entities.usuario import Usuario
    from src.database.config import SessionLocal
    db = SessionLocal()
    try:
        estudiantes = db.query(Estudiante).all()
        print("\n--- ESTUDIANTES DISPONIBLES ---")
        for e in estudiantes:
            print(f"  {e.usuario.nombre} | ID: {e.id_estudiante}")
        print()
    finally:
        db.close()


def mostrar_aulas():
    from src.entities.aula import Aula
    from src.database.config import SessionLocal
    db = SessionLocal()
    try:
        aulas = db.query(Aula).all()
        print("\n--- AULAS DISPONIBLES ---")
        for a in aulas:
            print(f"  {a.numero_aula} | Edificio: {a.edificio} | ID: {a.id_aula}")
        print()
    finally:
        db.close()


def mostrar_profesores():
    from src.entities.profesor import Profesor
    from src.database.config import SessionLocal
    db = SessionLocal()
    try:
        profesores = db.query(Profesor).all()
        print("\n--- PROFESORES DISPONIBLES ---")
        for p in profesores:
            print(f"  {p.usuario.nombre} | Especialidad: {p.especialidad} | ID: {p.id_profesor}")
        print()
    finally:
        db.close()


def menu_configuracion(admin_id: UUID):
    while True:
        print("\n--- CONFIGURACIÓN FÍSICA Y ACADÉMICA ---")
        print("1. Registrar Aula")
        print("2. Registrar Grado")
        print("3. Registrar Departamento")
        print("0. Volver")
        op = leer_texto(">> ")
        if op == "0":
            break
        elif op == "1":
            numero = leer_texto("Número de Aula: ")
            capacidad = leer_texto("Capacidad: ")
            edificio = leer_texto("Edificio: ")
            if numero and capacidad and edificio:
                aula = aula_crud.crear_aula(numero, capacidad, edificio, admin_id)
                print(f"Aula creada. ID: {aula.id_aula}")
            else:
                print("  [!] Todos los campos son obligatorios.")
        elif op == "2":
            nom = leer_texto("Nombre Grado (ej: 11-B): ")
            if nom:
                grado = grado_crud.crear_grado(nom, "Secundaria", "Mañana", admin_id)
                print(f"Grado creado. ID: {grado.id_grado}")
            else:
                print("  [!] El nombre del grado es obligatorio.")
        elif op == "3":
            nom = leer_texto("Nombre Departamento: ")
            tel = leer_texto("Teléfono: ")
            ofi = leer_texto("Oficina: ")
            if nom and tel and ofi:
                depto = departamento_crud.crear_departamento(nom, tel, ofi, admin_id)
                print(f"Departamento creado. ID: {depto.id_departamento}")
            else:
                print("  [!] Todos los campos son obligatorios.")


def menu_personas(admin_id: UUID):
    while True:
        print("\n--- GESTIÓN DE PERSONAS ---")
        print("1. Crear Perfil Estudiante")
        print("2. Crear Perfil Profesor")
        print("0. Volver")
        op = leer_texto(">> ")
        if op == "0":
            break
        elif op == "1":
            mostrar_usuarios()
            mostrar_grados()
            id_u = leer_uuid("ID del Usuario: ")
            id_g = leer_uuid("ID del Grado: ")
            if id_u and id_g:
                estudiante_crud.crear_estudiante(id_u, id_g, admin_id)
                print("Perfil de estudiante vinculado.")
            else:
                print("  [!] IDs inválidos o vacíos.")
        elif op == "2":
            mostrar_usuarios()
            mostrar_departamentos()
            id_u = leer_uuid("ID del Usuario: ")
            id_d = leer_uuid("ID del Departamento: ")
            esp = leer_texto("Especialidad: ")
            if id_u and id_d and esp:
                profesor_crud.crear_profesor(id_u, id_d, esp, admin_id)
                print("Perfil de profesor vinculado.")
            else:
                print("  [!] IDs inválidos o campos vacíos.")


def menu_academico(user_id: UUID):
    while True:
        print("\n--- CONTROL ACADÉMICO ---")
        print("1. Registrar Curso")
        print("2. Subir Calificación")
        print("3. Registrar Asistencia")
        print("0. Volver")
        op = leer_texto(">> ")
        if op == "0":
            break
        elif op == "1":
            mostrar_profesores()
            mostrar_grados()
            mostrar_aulas()
            nom = leer_texto("Nombre del Curso: ")
            id_p = leer_uuid("ID Profesor: ")
            id_g = leer_uuid("ID Grado: ")
            id_a = leer_uuid("ID Aula: ")
            if nom and id_p and id_g and id_a:
                curso = curso_crud.crear_curso(nom, id_p, id_g, id_a, user_id)
                print(f"Curso creado. ID: {curso.id_curso}")
            else:
                print("  [!] IDs inválidos o campos vacíos.")
        elif op == "2":
            mostrar_estudiantes()
            mostrar_cursos()
            id_e = leer_uuid("ID Estudiante: ")
            id_c = leer_uuid("ID Curso: ")
            nota = leer_texto("Nota: ")
            if id_e and id_c and nota:
                calificacion_crud.crear_calificacion(nota, id_e, id_c, user_id)
                print("Calificación guardada.")
            else:
                print("  [!] IDs inválidos o nota vacía.")
        elif op == "3":
            mostrar_estudiantes()
            mostrar_cursos()
            id_e = leer_uuid("ID Estudiante: ")
            id_c = leer_uuid("ID Curso: ")
            fecha = leer_texto("Fecha (YYYY-MM-DD): ")
            estado = leer_texto("Estado (PRESENTE/AUSENTE/TARDANZA): ")
            if id_e and id_c and fecha and estado:
                asistencia_crud.crear_asistencia(
                    datetime.datetime.fromisoformat(fecha),
                    estado,
                    id_e,
                    id_c,
                    user_id
                )
                print("Asistencia registrada.")
            else:
                print("  [!] IDs inválidos o campos vacíos.")


def main():
    usuario = login_sistema()
    if not usuario:
        return

    while True:
        print(f"\n========== MENU PRINCIPAL | Usuario: {usuario.nombre} ==========")
        print("1. Configuración (Grados, Aulas, Departamentos)")
        print("2. Personas (Estudiantes, Profesores)")
        print("3. Académico (Cursos, Notas, Asistencia)")
        print("0. Salir")

        op = leer_texto("Opción: ")
        if op == "0":
            break
        elif op == "1":
            menu_configuracion(usuario.id_usuario)
        elif op == "2":
            menu_personas(usuario.id_usuario)
        elif op == "3":
            menu_academico(usuario.id_usuario)


if __name__ == "__main__":
    main()