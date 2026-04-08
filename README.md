# 🎓 Backend-Escuela

Sistema backend para la gestión académica de una institución educativa. Permite administrar estudiantes, cursos, calificaciones, asistencia y más, ahora mediante una **API REST construida con FastAPI**.

---

## 🚀 Características

* CRUD completo para:

  * Estudiantes
  * Profesores
  * Cursos
  * Calificaciones
  * Asistencia
  * Departamentos
  * Horarios
  * Usuarios

* 🌐 API REST con FastAPI

* ⚡ Servidor ASGI con Uvicorn

* Validación de datos con Pydantic

* Manejo de errores con HTTPException

* Conexión a base de datos mediante Neon (PostgreSQL)

* Arquitectura modular y escalable

* Uso de Programación Orientada a Objetos

* Separación por capas (entities, crud, database, routers)

---

## 🏗️ Estructura del Proyecto

```
📁 src
│
├── 📁 crud
│   ├── asistencia_crud.py
│   ├── aula_crud.py
│   ├── calificacion_crud.py
│   ├── curso_crud.py
│   ├── departamento_crud.py
│   ├── director_crud.py
│   ├── estudiante_crud.py
│   ├── grado_crud.py
│   ├── horario_crud.py
│   ├── profesor_crud.py
│   └── usuario_crud.py
│
├── 📁 database
│   └── config.py
│
├── 📁 entities
│   ├── asistencia.py
│   ├── aula.py
│   ├── calificacion.py
│   ├── curso.py
│   ├── departamento.py
│   ├── director.py
│   ├── estudiante.py
│   ├── grado.py
│   ├── horario.py
│   ├── profesor.py
│   └── usuario.py
│
├── 📁 routers
│   ├── asistencia_router.py
│   ├── aula_router.py
│   ├── calificacion_router.py
│   ├── curso_router.py
│   ├── departamento_router.py
│   ├── director_router.py
│   ├── estudiante_router.py
│   ├── grado_router.py
│   ├── horario_router.py
│   ├── profesor_router.py
│   └── usuario_router.py
│
├── main.py
├── migrardb.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Arquitectura

El proyecto sigue una arquitectura modular basada en:

* **Entities** → Modelos del dominio
* **CRUD** → Lógica de acceso a datos
* **Routers** → Endpoints de la API
* **Database** → Conexión a PostgreSQL
* **Main** → Punto de entrada

### Tecnologías utilizadas

* FastAPI
* Uvicorn
* Pydantic
* PostgreSQL (Neon)

---

## 📡 Endpoints

* `GET /recurso` → Obtener todos
* `GET /recurso/{id}` → Obtener por ID
* `POST /recurso` → Crear
* `PUT /recurso/{id}` → Actualizar
* `DELETE /recurso/{id}` → Eliminar

---

## ⚙️ Requisitos

* Python 3.10 o superior
* PostgreSQL

---

## 📦 Instalación

Clonar repositorio:

```bash
git clone https://github.com/dahianamon12/Backend-Escuela
cd Backend-Escuela
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución

```bash
 python -m uvicorn main:app --reload
``` *
---

## 🎥 Video de explicación
https://correoitmedu-my.sharepoint.com/:v:/g/personal/isabelagonzalez1128290_correo_itm_edu_co/IQCh4YTl_ygvRKs9pZRlKkwEAY-hEGDS68vkea4BvbYsXKg?e=Rj3nmWnav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbE1vZGUiOiJtaXMiLCJyZWZlcnJhbFZpZXciOiJwb3N0cm9sbC1jb3B5bGluayIsInJlZmVycmFsUGxheWJhY2tTZXNzaW9uSWQiOiJjNTc2NmI0My0zZTRmLTQxMzMtOWJmNi1kZWEwMzg2MzJjOWEifX0%3D
---

## ✒️ Autoras

- Dahiana Montañez  
  https://github.com/dahianamon12  

- Isabela González  
  https://github.com/isagonzaleze17-cpu -