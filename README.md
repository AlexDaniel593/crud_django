# 🚨 CRUD Empleados con Vulnerabilidades de Seguridad

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://djangoproject.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green.svg)](https://mongodb.com)
[![License](https://img.shields.io/badge/License-Educational-red.svg)](#)

> ⚠️ **ADVERTENCIA**: Este proyecto contiene **vulnerabilidades de seguridad intencionadas** para fines educativos. **NO lo uses en producción**.

## 📚 Descripción

Este proyecto implementa un sistema CRUD completo para gestionar empleados usando Django como framework web y MongoDB como base de datos. El sistema incluye **vulnerabilidades de seguridad intencionadas** para demostrar malas prácticas de desarrollo y servir como herramienta educativa en ciberseguridad.

## 🎯 Propósito Educativo

Este proyecto está diseñado para:
- 📖 **Aprendizaje**: Demostrar vulnerabilidades comunes en aplicaciones web
- 🔍 **Análisis**: Identificar y entender problemas de seguridad
- 🛡️ **Entrenamiento**: Practicar técnicas de penetration testing
- 📊 **Investigación**: Estudiar el impacto de vulnerabilidades

## 🔐 Sistema de Autenticación

El sistema incluye un mecanismo de login con **vulnerabilidades de seguridad intencionadas**:

### **Credenciales por Defecto:**
- **Usuario:** `admin`
- **Contraseña:** `admin`

### **⚠️ Vulnerabilidades Implementadas:**
1. **Contraseñas sin cifrar** - Almacenadas en texto plano
2. **Información de errores expuesta** - Revela detalles del sistema
3. **Validación débil de sesión** - Verificación insegura
4. **Posible inyección NoSQL** - Sin sanitización de entradas
5. **Logs inseguros** - Contraseñas visibles en logs

## Características

- **CRUD completo**: Crear, Leer, Actualizar y Eliminar empleados
- **Interfaz web moderna**: Usando Bootstrap 5 y Font Awesome
- **API REST**: Endpoints JSON para integración con otras aplicaciones
- **MongoDB Atlas**: Conexión a cluster de MongoDB en la nube
- **Validación de datos**: Validación tanto en frontend como backend

## 🚀 Instalación y Configuración

### Prerequisitos
- Python 3.11+
- Git
- Cuenta de MongoDB Atlas (gratuita)

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/crud-empleados-vulnerabilidades.git
cd crud-empleados-vulnerabilidades
```

### 2. Crear Entorno Virtual
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno
```bash
cp .env.example .env
# Edita .env con tus credenciales de MongoDB
```

### 5. Configurar Base de Datos
```bash
python manage.py migrate
python crear_admin.py
```

### 6. Ejecutar el Servidor
```bash
# Opción 1: Script automático (Windows)
ejecutar_con_login.bat

# Opción 2: Manual
python manage.py runserver
```

### 7. Acceder al Sistema
1. Ve a: http://127.0.0.1:8000/
2. Ingresa las credenciales:
   - **Usuario:** `admin`
   - **Contraseña:** `admin`

## Configuración

### 1. Variables de Entorno

Edita el archivo `.env` y actualiza la contraseña de tu cluster MongoDB:

```env
MONGODB_URI=mongodb+srv://daxel203:TU_PASSWORD@cluster0.0xohifm.mongodb.net/
MONGODB_DATABASE=Investigacion
```

### 2. Instalación de Dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar Usuario Administrador

```bash
python crear_admin.py
```

### 4. Ejecutar el Servidor

**Opción A - Script automático:**
```bash
ejecutar_con_login.bat
```

**Opción B - Manual:**
```bash
python manage.py runserver
```

### 5. Acceder al Sistema

1. Ve a: http://127.0.0.1:8000/
2. Ingresa las credenciales:
   - **Usuario:** `admin`
   - **Contraseña:** `admin`

## Estructura del Proyecto

- **Modelo Empleado**: Definido con MongoEngine para trabajar con MongoDB
- **Vistas Web**: Interfaz completa para gestión de empleados
- **API REST**: Endpoints para operaciones CRUD
- **Templates**: Interfaz responsiva con Bootstrap

## Endpoints Disponibles

### Autenticación
- `/` - Redirección al login
- `/empleados/login/` - Página de login
- `/empleados/logout/` - Cerrar sesión

### Interfaz Web (Requiere Login Admin)
- `/empleados/` - Lista de empleados
- `/empleados/crear/` - Crear nuevo empleado
- `/empleados/detalle/<id>/` - Ver detalles del empleado
- `/empleados/editar/<id>/` - Editar empleado
- `/empleados/eliminar/<id>/` - Eliminar empleado

### API REST
- `GET /empleados/api/empleados/` - Obtener todos los empleados
- `GET /empleados/api/empleados/<id>/` - Obtener empleado específico
- `POST /empleados/api/empleados/crear/` - Crear nuevo empleado
- `PUT /empleados/api/empleados/actualizar/<id>/` - Actualizar empleado
- `DELETE /empleados/api/empleados/eliminar/<id>/` - Eliminar empleado

## Modelo de Datos

### **Usuario (Con Vulnerabilidades)**
El modelo `Usuario` incluye los siguientes campos:

- `username`: Nombre de usuario único (requerido)
- `password`: Contraseña **SIN CIFRAR** ⚠️ (requerido)
- `email`: Email del usuario
- `es_admin`: Si es administrador (Si/No)
- `ultimo_acceso`: Fecha del último acceso

### **Empleado**
El modelo `Empleado` incluye los siguientes campos:

- `nombre`: Nombre del empleado (requerido)
- `apellido`: Apellido del empleado (requerido)
- `email`: Email único (requerido)
- `telefono`: Número de teléfono
- `departamento`: Departamento de trabajo
- `cargo`: Cargo o posición
- `salario`: Salario del empleado
- `fecha_contratacion`: Fecha de contratación (automática)
- `activo`: Estado del empleado (Si/No)

## Uso de la API

### Crear un empleado (POST)
```json
{
    "nombre": "Juan",
    "apellido": "Pérez",
    "email": "juan.perez@example.com",
    "telefono": "0999123456",
    "departamento": "IT",
    "cargo": "Desarrollador",
    "salario": 2000.00,
    "activo": "Si"
}
```

### Actualizar un empleado (PUT)
```json
{
    "salario": 2500.00,
    "cargo": "Senior Developer"
}
```

## 📸 Screenshots

### Página de Login
![Login](docs/login.png)

### Dashboard de Empleados
![Dashboard](docs/dashboard.png)

## 🔗 Estructura del Proyecto

```
crud_django/
├── .env.example              # Variables de entorno de ejemplo
├── .gitignore               # Archivos a ignorar por Git
├── requirements.txt         # Dependencias de Python
├── manage.py               # Comando principal de Django
├── crear_admin.py          # Script para crear usuario admin
├── test_mongodb.py         # Script de prueba de MongoDB
├── ejecutar_con_login.bat  # Script de ejecución automática
├── crud_django/            # Configuración principal
│   ├── settings.py         # Configuración de Django
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # Configuración WSGI
└── empleados/             # App principal
    ├── models.py          # Modelos (Usuario y Empleado)
    ├── views.py           # Vistas y lógica de negocio
    ├── urls.py            # URLs de la app
    └── templates/         # Templates HTML
        └── empleados/
            ├── base.html
            ├── login.html
            ├── lista.html
            ├── crear.html
            ├── detalle.html
            ├── editar.html
            ├── eliminar.html
            └── error.html
```

## 🤝 Contribuciones

Este es un proyecto educativo. Las contribuciones son bienvenidas, especialmente:
- 🐛 Nuevas vulnerabilidades para demostrar
- 📚 Mejoras en la documentación
- 🔧 Optimizaciones de código
- 📝 Casos de prueba adicionales

## 📄 Licencia

Este proyecto es solo para **fines educativos**. No está destinado para uso en producción.

## ⚠️ Descargo de Responsabilidad

- Este software contiene vulnerabilidades **intencionadas**
- Solo para **educación** y **investigación**
- Los autores no se responsabilizan por el mal uso
- **NO usar en entornos de producción**

## 👨‍💻 Autor

Desarrollado para fines educativos en ciberseguridad y desarrollo seguro.

---

**¿Encontraste una vulnerabilidad? ¡Esa era la idea! 🎯**
