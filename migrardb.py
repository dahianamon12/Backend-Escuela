"""
Script para crear las tablas en Neon (PostgreSQL).
Ejecutar una vez después de configurar DATABASE_URL en .env:

  python migrardb.py

No es necesario levantar la API; este script solo aplica el esquema.
"""

import os

from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

# Ahora sí se pueden importar los modelos (registrarlos en Base.metadata)
import src.entities.asistencia  # noqa: F401
import src.entities.aula  # noqa: F401
import src.entities.calificacion  # noqa: F401
import src.entities.curso  # noqa: F401
import src.entities.departamento  # noqa: F401
import src.entities.director  # noqa: F401
import src.entities.estudiante  # noqa: F401
import src.entities.grado  # noqa: F401
import src.entities.horario  # noqa: F401
import src.entities.profesor  # noqa: F401
import src.entities.usuario  # noqa: F401

from src.database.config import create_tables

try:
    create_tables()
    print("✅ Tablas creadas correctamente en Neon.")
except OperationalError as e:
    if "password authentication failed" in str(e).lower():
        print(" Error: Neon rechazó la contraseña (password authentication failed).")
        print(
            "  - Entra a https://console.neon.tech y revisa la conexión del proyecto."
        )
        print("  - Copia de nuevo la connection string y actualiza .env.")
        print(
            "  - Si la contraseña tiene caracteres especiales (& # @ ?), codifícala en URL (ej. @ → %40)."
        )
    else:
        print(" Error de conexión a la base de datos:", e)
    raise SystemExit(1)
