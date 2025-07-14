#!/usr/bin/env python
"""
Script para probar la conexión a MongoDB y agregar datos de ejemplo
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

from empleados.models import Empleado


def test_connection():
    """Prueba la conexión a MongoDB"""
    try:
        # Intentar contar documentos existentes
        count = Empleado.objects.count()
        print(f"✅ Conexión exitosa a MongoDB!")
        print(f"📊 Empleados existentes en la base de datos: {count}")
        return True
    except Exception as e:
        print(f"❌ Error de conexión a MongoDB: {e}")
        return False


def create_sample_data():
    """Crea datos de ejemplo si no existen"""
    try:
        if Empleado.objects.count() == 0:
            empleados_ejemplo = [
                {
                    'nombre': 'Juan',
                    'apellido': 'Pérez',
                    'email': 'juan.perez@empresa.com',
                    'telefono': '0999123456',
                    'departamento': 'Desarrollo',
                    'cargo': 'Desarrollador Senior',
                    'salario': 2500.00,
                    'activo': 'Si'
                },
                {
                    'nombre': 'María',
                    'apellido': 'González',
                    'email': 'maria.gonzalez@empresa.com',
                    'telefono': '0987654321',
                    'departamento': 'Recursos Humanos',
                    'cargo': 'Gerente de RRHH',
                    'salario': 3000.00,
                    'activo': 'Si'
                },
                {
                    'nombre': 'Carlos',
                    'apellido': 'Rodríguez',
                    'email': 'carlos.rodriguez@empresa.com',
                    'telefono': '0912345678',
                    'departamento': 'Marketing',
                    'cargo': 'Especialista en Marketing',
                    'salario': 2000.00,
                    'activo': 'Si'
                }
            ]
            
            for empleado_data in empleados_ejemplo:
                empleado = Empleado(**empleado_data)
                empleado.save()
                print(f"✅ Empleado creado: {empleado.nombre} {empleado.apellido}")
            
            print(f"🎉 Se crearon {len(empleados_ejemplo)} empleados de ejemplo")
        else:
            print("ℹ️  Ya existen empleados en la base de datos")
            
    except Exception as e:
        print(f"❌ Error al crear datos de ejemplo: {e}")


def list_employees():
    """Lista todos los empleados"""
    try:
        empleados = Empleado.objects.all()
        print("\n📋 Lista de empleados:")
        print("-" * 80)
        for empleado in empleados:
            print(f"• {empleado.nombre} {empleado.apellido}")
            print(f"  Email: {empleado.email}")
            print(f"  Departamento: {empleado.departamento}")
            print(f"  Cargo: {empleado.cargo}")
            print(f"  Salario: ${empleado.salario}")
            print(f"  Estado: {empleado.activo}")
            print(f"  ID: {empleado.id}")
            print("-" * 80)
    except Exception as e:
        print(f"❌ Error al listar empleados: {e}")


if __name__ == "__main__":
    print("🔧 Probando conexión a MongoDB...")
    
    if test_connection():
        print("\n🚀 Creando datos de ejemplo...")
        create_sample_data()
        
        print("\n📊 Listando empleados...")
        list_employees()
        
        print(f"\n✅ Todo listo! Puedes visitar http://127.0.0.1:8000/ para ver la aplicación")
    else:
        print("\n❌ No se pudo conectar a MongoDB.")
        print("📝 Verifica que:")
        print("   1. El archivo .env tenga la URL correcta de MongoDB")
        print("   2. La contraseña en la URL sea correcta")
        print("   3. Tu IP esté en la lista blanca del cluster de MongoDB")
