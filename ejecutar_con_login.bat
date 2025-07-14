@echo off
echo.
echo ===============================================
echo    🔐 CRUD Django con Sistema de Login
echo    ⚠️  CON VULNERABILIDADES INTENCIONADAS
echo ===============================================
echo.

cd /d "C:\Users\dalex\OneDrive\Documentos\ESPE\Investigacion\parcial 2\crud_django"

echo 🔧 Verificando configuración...
"C:/Users/dalex/OneDrive/Documentos/ESPE/Investigacion/parcial 2/crud_django/.venv/Scripts/python.exe" manage.py check

if %ERRORLEVEL% NEQ 0 (
    echo ❌ Error en la configuración
    pause
    exit /b 1
)

echo ✅ Configuración correcta
echo.

echo �️ Aplicando migraciones de Django...
"C:/Users/dalex/OneDrive/Documentos/ESPE/Investigacion/parcial 2/crud_django/.venv/Scripts/python.exe" manage.py migrate

echo.
echo �👤 Configurando usuario administrador...
"C:/Users/dalex/OneDrive/Documentos/ESPE/Investigacion/parcial 2/crud_django/.venv/Scripts/python.exe" crear_admin.py

echo.
echo 🚀 Iniciando servidor...
echo.
echo 📱 ACCESO AL SISTEMA:
echo    URL: http://127.0.0.1:8000/
echo    Usuario: admin
echo    Contraseña: admin
echo.
echo 🔐 FUNCIONALIDADES:
echo    • Sistema de login con vulnerabilidades
echo    • CRUD completo de empleados
echo    • Solo usuarios admin pueden acceder
echo    • API REST disponible
echo.
echo ⚠️  VULNERABILIDADES IMPLEMENTADAS:
echo    • Contraseñas sin cifrar
echo    • Información de errores expuesta
echo    • Validación débil de sesión
echo    • Posible inyección NoSQL
echo.
echo 📝 Presiona Ctrl+C para detener el servidor
echo.

"C:/Users/dalex/OneDrive/Documentos/ESPE/Investigacion/parcial 2/crud_django/.venv/Scripts/python.exe" manage.py runserver

echo.
echo 👋 Servidor detenido
pause
