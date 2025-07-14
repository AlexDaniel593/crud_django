from mongoengine import Document, StringField, IntField, FloatField, DateTimeField
from datetime import datetime


class Usuario(Document):
    """
    Modelo para representar un usuario del sistema (CON VULNERABILIDADES INTENCIONADAS)
    NOTA: Este modelo tiene vulnerabilidades de seguridad para fines educativos
    """
    username = StringField(max_length=50, required=True, unique=True)
    password = StringField(max_length=100, required=True)  # ¡SIN CIFRAR! - VULNERABILIDAD
    email = StringField(max_length=200)
    es_admin = StringField(max_length=10, default='No', choices=['Si', 'No'])
    ultimo_acceso = DateTimeField()
    
    # Configuración de la colección
    meta = {
        'collection': 'usuario',
        'db_alias': 'default'
    }
    
    def __str__(self):
        return f"{self.username}"
    
    def verificar_password(self, password):
        """VULNERABILIDAD: Comparación directa sin cifrado"""
        return self.password == password
    
    def to_dict(self):
        """Convierte el documento a diccionario para JSON"""
        return {
            'id': str(self.id),
            'username': self.username,
            'email': self.email,
            'es_admin': self.es_admin,
            'ultimo_acceso': self.ultimo_acceso.isoformat() if self.ultimo_acceso else None
        }


class Empleado(Document):
    """
    Modelo para representar un empleado en MongoDB
    """
    nombre = StringField(max_length=100, required=True)
    apellido = StringField(max_length=100, required=True)
    email = StringField(max_length=200, required=True, unique=True)
    telefono = StringField(max_length=20)
    departamento = StringField(max_length=100)
    cargo = StringField(max_length=100)
    salario = FloatField()
    fecha_contratacion = DateTimeField(default=datetime.now)
    activo = StringField(max_length=10, default='Si', choices=['Si', 'No'])
    
    # Configuración de la colección
    meta = {
        'collection': 'empleado',
        'db_alias': 'default'
    }
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def to_dict(self):
        """Convierte el documento a diccionario para JSON"""
        return {
            'id': str(self.id),
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'departamento': self.departamento,
            'cargo': self.cargo,
            'salario': self.salario,
            'fecha_contratacion': self.fecha_contratacion.isoformat() if self.fecha_contratacion else None,
            'activo': self.activo
        }
