# 🚨 CRUD Empleados con Vulnerabilidades de Seguridad

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://djangoproject.com)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green.svg)](https://mongodb.com)
[![License](https://img.shields.io/badge/License-Educational-red.svg)](#)

> ⚠️ **ADVERTENCIA**: Este proyecto contiene **vulnerabilidades de seguridad intencionadas** para fines educativos. **NO lo uses en producción**.

## 📚 Descripción

Este proyecto implementa un sistema CRUD completo para gestionar empleados usando Django como framework web y MongoDB Atlas como base de datos. El sistema incluye **vulnerabilidades de seguridad intencionadas** para demostrar malas prácticas de desarrollo y servir como herramienta educativa en ciberseguridad.

**Repositorio:** https://github.com/AlexDaniel593/crud_django.git

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
- **Sistema de Login**: Autenticación con vulnerabilidades intencionadas
- **Interfaz web moderna**: Usando Bootstrap 5 y Font Awesome
- **API REST**: Endpoints JSON para integración con otras aplicaciones
- **MongoDB Atlas**: Conexión a cluster de MongoDB en la nube
- **Validación de datos**: Validación tanto en frontend como backend (con fallas intencionadas)

## 🚀 Instalación y Configuración

### Prerequisitos
- Python 3.11+
- Git
- Cuenta de MongoDB Atlas (gratuita)

### 1. Clonar el Repositorio
```bash
git clone https://github.com/AlexDaniel593/crud_django.git
cd crud_django
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
# Copia el archivo de ejemplo y configura tus credenciales
copy .env.example .env
# Edita .env con tu URL de MongoDB Atlas
```

**Ejemplo de configuración .env:**
```env
MONGODB_URI=mongodb+srv://tu_usuario:tu_password@cluster0.xxxxx.mongodb.net/
MONGODB_DATABASE=Investigacion
```

### 5. Aplicar Migraciones y Configurar Base de Datos
```bash
python manage.py migrate
python crear_admin.py
```

### 6. Crear Datos de Ejemplo (Opcional)
```bash
python test_mongodb.py
```

### 7. Ejecutar el Servidor
```bash
python manage.py runserver
```

### 8. Acceder al Sistema
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
├── .env                     # Variables de entorno (NO incluido en Git)
├── .env.example            # Ejemplo de variables de entorno
├── .gitignore              # Archivos a ignorar por Git
├── requirements.txt        # Dependencias de Python
├── manage.py              # Comando principal de Django
├── crear_admin.py         # Script para crear usuario admin
├── test_mongodb.py        # Script de prueba de MongoDB
├── ejecutar_con_login.bat # Script de ejecución automática (Windows)
├── crud_django/           # Configuración principal del proyecto
│   ├── __init__.py
│   ├── settings.py        # Configuración de Django y MongoDB
│   ├── urls.py           # URLs principales
│   ├── wsgi.py          # Configuración WSGI
│   └── asgi.py          # Configuración ASGI
└── empleados/            # App principal de empleados
    ├── __init__.py
    ├── models.py         # Modelos (Usuario y Empleado)
    ├── views.py          # Vistas y lógica de negocio
    ├── urls.py           # URLs de la app
    ├── apps.py           # Configuración de la app
    ├── admin.py          # Configuración del admin
    ├── tests.py          # Tests (vacío)
    └── templates/        # Templates HTML
        └── empleados/
            ├── base.html      # Template base
            ├── login.html     # Página de login
            ├── lista.html     # Lista de empleados
            ├── crear.html     # Crear empleado
            ├── detalle.html   # Detalles del empleado
            ├── editar.html    # Editar empleado
            ├── eliminar.html  # Confirmar eliminación
            └── error.html     # Página de error
```

## 📊 Base de Datos MongoDB

### Colecciones:
- **`empleado`**: Almacena información de empleados
- **`usuario`**: Almacena usuarios del sistema (con vulnerabilidades)

### Modelo Empleado:
- `nombre`: Nombre del empleado (requerido)
- `apellido`: Apellido del empleado (requerido)
- `email`: Email único (requerido)
- `telefono`: Número de teléfono
- `departamento`: Departamento de trabajo
- `cargo`: Cargo o posición
- `salario`: Salario del empleado
- `fecha_contratacion`: Fecha de contratación (automática)
- `activo`: Estado del empleado (Si/No)

### Modelo Usuario (Con Vulnerabilidades):
- `username`: Nombre de usuario único (requerido)
- `password`: Contraseña **SIN CIFRAR** ⚠️ (requerido)
- `email`: Email del usuario
- `es_admin`: Si es administrador (Si/No)
- `ultimo_acceso`: Fecha del último acceso

## 🛠️ Scripts Disponibles

### `ejecutar_con_login.bat` (Windows)
Script que automatiza todo el proceso:
- Verifica la configuración
- Aplica migraciones
- Crea el usuario admin
- Inicia el servidor

### `crear_admin.py`
Crea el usuario administrador con vulnerabilidades intencionadas:
```bash
python crear_admin.py
```

### `test_mongodb.py`
Prueba la conexión a MongoDB y crea empleados de ejemplo:
```bash
python test_mongodb.py
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

Desarrollado por AlexDaniel593 para fines educativos en ciberseguridad y desarrollo seguro.

---

**¿Encontraste una vulnerabilidad? ¡Esa era la idea! 🎯**
