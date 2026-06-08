# Erick Software Portfolio

Portfolio profesional de **Erick Manuel Rodríguez López**, Ingeniero de Software y Full-Stack Developer.

El proyecto está diseñado para presentar experiencia profesional, proyectos reales, tecnologías, educación, fortalezas y medios de contacto mediante una interfaz moderna, responsive y administrable.

El contenido público puede gestionarse desde un panel privado construido con Django Admin, sin necesidad de modificar directamente el código del frontend.

---

## Características principales

* Portfolio profesional responsive.
* Diseño oscuro, moderno y minimalista.
* Fotografía de perfil administrable.
* Información personal editable.
* Gestión de proyectos mediante CRUD.
* Proyectos mostrados en grupos de tres.
* Experiencia profesional con carga progresiva.
* Stack tecnológico organizado por categorías.
* Fortalezas profesionales.
* Educación y certificaciones.
* Enlaces de GitHub, LinkedIn y correo.
* SEO básico administrable.
* Secciones configurables y ordenables.
* Panel administrativo privado.
* API pública de solo lectura.
* Separación completa entre backend y frontend.
* Preparado para despliegue en Ubuntu Server.

---

## Tecnologías utilizadas

### Backend

* Python
* Django
* Django REST Framework
* django-filter
* django-cors-headers
* django-environ
* Psycopg
* Pillow
* PostgreSQL

### Frontend

* React
* TypeScript
* Vite
* React Router
* Motion
* Lucide React
* React Icons
* CSS modular organizado por secciones

### Herramientas

* Git
* GitHub
* Visual Studio Code
* PostgreSQL
* pgAdmin 4
* PowerShell
* Linux / Ubuntu Server

---

## Arquitectura general

El proyecto utiliza una arquitectura separada:

```text
ErickSoftware/
├── backend/
│   ├── apps/
│   │   ├── accounts/
│   │   ├── common/
│   │   └── portfolio/
│   ├── config/
│   ├── media/
│   ├── static/
│   ├── templates/
│   ├── manage.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── app/
│   │   ├── features/
│   │   ├── shared/
│   │   └── styles/
│   ├── package.json
│   ├── package-lock.json
│   └── .env.example
│
├── .gitignore
└── README.md
```

---

## Requisitos previos

Versiones utilizadas durante el desarrollo:

* Python 3.14
* Node.js 22
* npm 10
* PostgreSQL
* Git

También se recomienda tener instalado:

* pgAdmin 4
* Visual Studio Code

---

# Instalación local

## 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd ErickSoftware
```

---

# Configuración del backend

## 2. Entrar al backend

```bash
cd backend
```

## 3. Crear el entorno virtual

### Windows PowerShell

```powershell
py -m venv venv
.\venv\Scripts\activate
```

### Linux / Ubuntu

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Actualizar herramientas de Python

```bash
python -m pip install --upgrade pip setuptools wheel
```

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 6. Crear el archivo de entorno

### Windows PowerShell

```powershell
Copy-Item .env.example .env
```

### Linux / Ubuntu

```bash
cp .env.example .env
```

Después configura las variables reales dentro de:

```text
backend/.env
```

Ejemplo:

```env
DEBUG=True
SECRET_KEY=

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=5432

ALLOWED_HOSTS=127.0.0.1,localhost

CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
CSRF_TRUSTED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173

ADMIN_URL=
```

El archivo `.env` no debe subirse al repositorio.

---

# Base de datos PostgreSQL

## 7. Crear la base de datos

Puede crearse desde pgAdmin 4 o desde PostgreSQL.

Ejemplo:

```sql
CREATE DATABASE erick_portfolio;
```

La base de datos y las credenciales utilizadas deben coincidir con las variables configuradas en `backend/.env`.

---

## 8. Ejecutar migraciones

```bash
python manage.py migrate
```

## 9. Crear usuario administrador

```bash
python manage.py createsuperuser
```

## 10. Cargar datos iniciales

```bash
python manage.py seed_portfolio
```

Este comando carga contenido inicial para el perfil, tecnologías, proyectos, experiencia y otras secciones.

---

## 11. Verificar Django

```bash
python manage.py check
```

## 12. Ejecutar pruebas

```bash
python manage.py test apps.portfolio
```

## 13. Iniciar el backend

```bash
python manage.py runserver
```

La API quedará disponible en:

```text
http://127.0.0.1:8000
```

Endpoints públicos principales:

```text
GET /api/health/
GET /api/v1/portfolio/
GET /api/v1/projects/
GET /api/v1/projects/<slug>/
```

La ruta del administrador se configura mediante la variable:

```env
ADMIN_URL=
```

No debe publicarse directamente en la documentación.

---

# Configuración del frontend

## 14. Entrar al frontend

Desde la raíz del proyecto:

```bash
cd frontend
```

## 15. Instalar dependencias

```bash
npm ci
```

## 16. Crear el archivo de entorno

### Windows PowerShell

```powershell
Copy-Item .env.example .env
```

### Linux / Ubuntu

```bash
cp .env.example .env
```

Contenido esperado:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000/api/v1
```

## 17. Iniciar React

```bash
npm run dev
```

El frontend estará disponible normalmente en:

```text
http://localhost:5173
```

---

# Comandos de validación

## Backend

```bash
python manage.py check
python manage.py test apps.portfolio
```

## Frontend

```bash
npm run lint
npm run build
```

---

# Gestión del contenido

El panel privado permite administrar:

* Perfil del sitio.
* Fotografía de perfil.
* Nombre y título profesional.
* Resumen del hero.
* Texto de contacto.
* Proyectos.
* Imágenes de proyectos.
* Tecnologías.
* Categorías tecnológicas.
* Experiencia profesional.
* Educación.
* Certificaciones.
* Fortalezas profesionales.
* Enlaces sociales.
* Configuración SEO.
* Títulos y orden de las secciones.

Los elementos pueden marcarse como visibles u ocultos.

El frontend público solo muestra información visible.

---

# Archivos multimedia

Los archivos cargados desde Django se almacenan en:

```text
backend/media/
```

Esta carpeta no se incluye en Git.

En producción debe configurarse almacenamiento persistente y una estrategia de respaldo para:

* Fotografías de perfil.
* Portadas de proyectos.
* Galerías.
* Logotipos.
* Certificaciones.
* Currículum.

---

# Seguridad

* Las variables sensibles se almacenan en `.env`.
* La ruta del administrador es configurable.
* El administrador requiere autenticación.
* La API pública es de solo lectura.
* Los archivos `.env` están excluidos mediante `.gitignore`.
* Las credenciales de PostgreSQL no deben incluirse en GitHub.
* En producción debe utilizarse HTTPS.
* `DEBUG` debe configurarse como `False` en producción.
* `ALLOWED_HOSTS` debe limitarse a los dominios utilizados.
* La clave `SECRET_KEY` debe ser única y segura.

---

# Build de producción del frontend

```bash
npm run build
```

Los archivos compilados se generan en:

```text
frontend/dist/
```

La carpeta `dist` no se guarda en Git porque debe generarse durante el despliegue.

---

# Despliegue previsto

El proyecto está preparado para desplegarse en un servidor Ubuntu utilizando:

* PostgreSQL
* Python virtual environment
* Gunicorn
* Nginx
* Node.js para compilar React
* HTTPS
* Variables de entorno de producción
* Archivos estáticos de Django
* Archivos multimedia persistentes

La configuración de producción se documentará por separado.

---

# Autor

**Erick Manuel Rodríguez López**

Software Engineer / Full-Stack Developer

---

# Licencia

Este proyecto corresponde al portfolio personal de Erick Manuel Rodríguez López.

El código no debe reutilizarse, redistribuirse o publicarse como propio sin autorización.
