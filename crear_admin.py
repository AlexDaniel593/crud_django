#!/usr/bin/env python
"""
Script para crear el usuario administrador con vulnerabilidades
"""
import os
import sys
import django
from pathlib import Path

# Configurar Django
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud_django.settings')
django.setup()

from empleados.models import Usuario


def crear_usuario_admin():
    """Crea el usuario administrador con vulnerabilidades intencionadas"""
    try:
        # Verificar si ya existe el usuario admin
        try:
            usuario = Usuario.objects.get(username='admin')
            print(f"⚠️  El usuario 'admin' ya existe")
            print(f"🔑 Password actual: {usuario.password}")  # ¡VULNERABILIDAD: Mostrar password!
            return
        except:
            pass
        
        # Crear usuario admin con VULNERABILIDADES
        usuario_admin = Usuario(
            username='admin',
            password='admin',  # ¡VULNERABILIDAD: Password sin cifrar!
            email='admin@empresa.com',
            es_admin='Si'
        )
        usuario_admin.save()
        
        print("✅ Usuario administrador creado con VULNERABILIDADES:")
        print(f"👤 Usuario: admin")
        print(f"🔑 Contraseña: admin")  # ¡VULNERABILIDAD: Mostrar password en logs!
        print(f"📧 Email: admin@empresa.com")
        print(f"🛡️  Es Admin: Si")
        print(f"📄 ID: {usuario_admin.id}")
        
        print("\n⚠️  VULNERABILIDADES IMPLEMENTADAS:")
        print("   • Contraseña almacenada en texto plano")
        print("   • Credenciales mostradas en logs")
        print("   • Sin validación de fortaleza de contraseña")
        print("   • Sin límite de intentos de login")
        
    except Exception as e:
        print(f"❌ Error al crear usuario: {e}")


def listar_usuarios():
    """Lista todos los usuarios (VULNERABLE)"""
    try:
        usuarios = Usuario.objects.all()
        print(f"\n👥 Usuarios en el sistema ({usuarios.count()}):")
        print("-" * 60)
        
        for usuario in usuarios:
            print(f"• Usuario: {usuario.username}")
            print(f"  Contraseña: {usuario.password}")  # ¡VULNERABILIDAD: Mostrar passwords!
            print(f"  Email: {usuario.email}")
            print(f"  Es Admin: {usuario.es_admin}")
            print(f"  ID: {usuario.id}")
            print("-" * 60)
            
    except Exception as e:
        print(f"❌ Error al listar usuarios: {e}")


if __name__ == "__main__":
    print("🔧 Configurando usuario administrador...")
    print("⚠️  ESTE SCRIPT CONTIENE VULNERABILIDADES INTENCIONADAS")
    print()
    
    crear_usuario_admin()
    listar_usuarios()
    
    print("\n🚀 Sistema listo para usar:")
    print("   • Ve a: http://127.0.0.1:8000/login/")
    print("   • Usuario: admin")
    print("   • Contraseña: admin")
    print("\n📚 Este sistema muestra vulnerabilidades comunes:")
    print("   1. Almacenamiento de contraseñas en texto plano")
    print("   2. Exposición de información sensible en logs")
    print("   3. Validación débil de autenticación")
    print("   4. Falta de sanitización de entradas")
    print("   5. Exposición de errores del sistema")
