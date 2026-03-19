# 🎓 Backend-Escuela

Sistema backend para la gestión académica de una institución educativa. Permite administrar estudiantes, cursos, calificaciones, asistencia y más, utilizando Python y conexión a base de datos.

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
* Conexión a base de datos mediante **Neon (PostgreSQL)**
* Validación de datos con **Pydantic**
* Arquitectura modular y escalable
* Uso de Programación Orientada a Objetos
* Separación por capas (entities, crud, database)

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

* **Entities** → Modelos del dominio (POO + validaciones con Pydantic)
* **CRUD** → Lógica de acceso y manipulación de datos
* **Database** → Configuración de conexión a PostgreSQL (Neon)
* **Main** → Punto de entrada del sistema

### Conceptos aplicados:

* Programación Orientada a Objetos (POO)
* Encapsulamiento
* Separación de responsabilidades
* Validación de datos con Pydantic
* Manejo de variables de entorno (.env)

---

## ⚙️ Requisitos

* Python 3.10 o superior
* PostgreSQL (Neon recomendado)

---

## 📦 Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/dahianamon12/Backend-Escuela
cd Backend-Escuela
```

2. Crear entorno virtual:

```bash
python -m venv venv
```

3. Activar entorno virtual:

* Windows:

```bash
venv\Scripts\activate
```

* Linux / Mac:

```bash
source venv/bin/activate
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuración de variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```
DATABASE_URL=postgresql://usuario:password@host:puerto/database
```

(Usa tu conexión proporcionada por Neon)

---

## 🗄️ Migración / Inicialización de la Base de Datos

Ejecuta:

```bash
python migrardb.py
```

Esto creará las tablas necesarias en la base de datos.

---

## ▶️ Ejecución del Proyecto

```bash
python main.py

```

---

## ✒️ Autoras

* **Dahiana Montañez**
  https://github.com/dahianamon12

* **Isabela González**
  https://github.com/isagonzaleze17-cpu

---

## 📌 Notas

* Asegúrate de tener correctamente configurado el archivo `.env`
* No subir `.env` al repositorio (ya está incluido en `.gitignore`)
* Proyecto con fines académicos, pero con estructura profesional escalable
* link de la explicacion: https://correoitmedu-my.sharepoint.com/:v:/g/personal/dahianamontanez1129260_correo_itm_edu_co/IQDivmx9CZhESKx5QMjwARsVAdDwaTeSqOlRzectNSDfnqY?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=0eJz5d
