import sys

sys.path.insert(0, ".")

import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ← agregar

import src.entities.usuario
import src.entities.departamento
import src.entities.grado
import src.entities.aula
import src.entities.profesor
import src.entities.director
import src.entities.estudiante
import src.entities.curso
import src.entities.calificacion
import src.entities.asistencia
import src.entities.horario

from src.routers.usuario_router import router as usuario_router
from src.routers.aula_router import router as aula_router
from src.routers.grado_router import router as grado_router
from src.routers.departamento_router import router as departamento_router
from src.routers.estudiante_router import router as estudiante_router
from src.routers.profesor_router import router as profesor_router
from src.routers.director_router import router as director_router
from src.routers.curso_router import router as curso_router
from src.routers.calificacion_router import router as calificacion_router
from src.routers.asistencia_router import router as asistencia_router
from src.routers.horario_router import router as horario_router

app = FastAPI(
    title="API Escuela",
    description="Sistema de gestión escolar – ORM + FastAPI + Neon PostgreSQL",
    version="1.0.0",
)
origins = [
    "https://escuela-final.web.app",
    "https://escuela-final.firebaseapp.com",
    "http://localhost:4200",
]

# Aplicar las reglas de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ← agregar esto antes de los routers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario_router)
app.include_router(aula_router)
app.include_router(grado_router)
app.include_router(departamento_router)
app.include_router(estudiante_router)
app.include_router(profesor_router)
app.include_router(director_router)
app.include_router(curso_router)
app.include_router(calificacion_router)
app.include_router(asistencia_router)
app.include_router(horario_router)


@app.get("/", tags=["Root"])
def root():
    return {"mensaje": "API Escuela funcionando", "docs": "/docs"}
