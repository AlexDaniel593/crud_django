from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from mongoengine.errors import DoesNotExist, ValidationError
from bson import ObjectId
import json
from datetime import datetime
from .models import Empleado, Usuario


def login_view(request):
    """Vista de login con VULNERABILIDADES para fines educativos"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # VULNERABILIDAD: Sin sanitización de entrada
        # VULNERABILIDAD: Posible inyección NoSQL
        try:
            # Búsqueda directa sin validación
            usuario = Usuario.objects.get(username=username)
            
            # VULNERABILIDAD: Password sin cifrar
            if usuario.verificar_password(password):
                # Actualizar último acceso
                usuario.ultimo_acceso = datetime.now()
                usuario.save()
                
                # VULNERABILIDAD: Información sensible en sesión
                request.session['user_id'] = str(usuario.id)
                request.session['username'] = usuario.username
                request.session['es_admin'] = usuario.es_admin
                request.session['is_authenticated'] = True
                
                return redirect('lista_empleados')
            else:
                error = 'Credenciales incorrectas'
        except DoesNotExist:
            # VULNERABILIDAD: Información que revela existencia de usuarios
            error = 'Usuario no encontrado'
        except Exception as e:
            # VULNERABILIDAD: Exposición de errores internos
            error = f'Error interno: {str(e)}'
            
        return render(request, 'empleados/login.html', {'error': error})
    
    return render(request, 'empleados/login.html')


def logout_view(request):
    """Vista para cerrar sesión"""
    request.session.flush()
    return redirect('login')


def verificar_autenticacion(request):
    """Verificar si el usuario está autenticado (VULNERABLE)"""
    # VULNERABILIDAD: Verificación débil de sesión
    return request.session.get('is_authenticated', False)


def verificar_admin(request):
    """Verificar si el usuario es admin (VULNERABLE)"""
    # VULNERABILIDAD: Verificación basada solo en sesión
    return request.session.get('es_admin') == 'Si'


def lista_empleados(request):
    """Vista para mostrar la lista de empleados (SOLO ADMIN)"""
    if not verificar_autenticacion(request):
        return redirect('login')
    
    if not verificar_admin(request):
        return render(request, 'empleados/error.html', {'mensaje': 'Acceso denegado. Solo administradores.'})
    
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista.html', {
        'empleados': empleados,
        'usuario_actual': request.session.get('username')
    })


def detalle_empleado(request, empleado_id):
    """Vista para mostrar el detalle de un empleado"""
    if not verificar_autenticacion(request):
        return redirect('login')
    
    if not verificar_admin(request):
        return render(request, 'empleados/error.html', {'mensaje': 'Acceso denegado. Solo administradores.'})
    
    try:
        empleado = Empleado.objects.get(id=empleado_id)
        return render(request, 'empleados/detalle.html', {
            'empleado': empleado,
            'usuario_actual': request.session.get('username')
        })
    except DoesNotExist:
        return render(request, 'empleados/error.html', {'mensaje': 'Empleado no encontrado'})


def crear_empleado(request):
    """Vista para crear un nuevo empleado"""
    if not verificar_autenticacion(request):
        return redirect('login')
    
    if not verificar_admin(request):
        return render(request, 'empleados/error.html', {'mensaje': 'Acceso denegado. Solo administradores.'})
    
    if request.method == 'POST':
        try:
            empleado = Empleado(
                nombre=request.POST.get('nombre'),
                apellido=request.POST.get('apellido'),
                email=request.POST.get('email'),
                telefono=request.POST.get('telefono'),
                departamento=request.POST.get('departamento'),
                cargo=request.POST.get('cargo'),
                salario=float(request.POST.get('salario', 0)),
                activo=request.POST.get('activo', 'Si')
            )
            empleado.save()
            return redirect('lista_empleados')
        except ValidationError as e:
            return render(request, 'empleados/crear.html', {
                'error': str(e),
                'usuario_actual': request.session.get('username')
            })
        except ValueError:
            return render(request, 'empleados/crear.html', {
                'error': 'Salario debe ser un número válido',
                'usuario_actual': request.session.get('username')
            })
    
    return render(request, 'empleados/crear.html', {
        'usuario_actual': request.session.get('username')
    })


def editar_empleado(request, empleado_id):
    """Vista para editar un empleado existente"""
    if not verificar_autenticacion(request):
        return redirect('login')
    
    if not verificar_admin(request):
        return render(request, 'empleados/error.html', {'mensaje': 'Acceso denegado. Solo administradores.'})
    
    try:
        empleado = Empleado.objects.get(id=empleado_id)
        
        if request.method == 'POST':
            try:
                empleado.nombre = request.POST.get('nombre')
                empleado.apellido = request.POST.get('apellido')
                empleado.email = request.POST.get('email')
                empleado.telefono = request.POST.get('telefono')
                empleado.departamento = request.POST.get('departamento')
                empleado.cargo = request.POST.get('cargo')
                empleado.salario = float(request.POST.get('salario', 0))
                empleado.activo = request.POST.get('activo', 'Si')
                empleado.save()
                return redirect('lista_empleados')
            except ValidationError as e:
                return render(request, 'empleados/editar.html', {
                    'empleado': empleado, 
                    'error': str(e),
                    'usuario_actual': request.session.get('username')
                })
            except ValueError:
                return render(request, 'empleados/editar.html', {
                    'empleado': empleado, 
                    'error': 'Salario debe ser un número válido',
                    'usuario_actual': request.session.get('username')
                })
        
        return render(request, 'empleados/editar.html', {
            'empleado': empleado,
            'usuario_actual': request.session.get('username')
        })
    
    except DoesNotExist:
        return render(request, 'empleados/error.html', {'mensaje': 'Empleado no encontrado'})


def eliminar_empleado(request, empleado_id):
    """Vista para eliminar un empleado"""
    if not verificar_autenticacion(request):
        return redirect('login')
    
    if not verificar_admin(request):
        return render(request, 'empleados/error.html', {'mensaje': 'Acceso denegado. Solo administradores.'})
    
    try:
        empleado = Empleado.objects.get(id=empleado_id)
        
        if request.method == 'POST':
            empleado.delete()
            return redirect('lista_empleados')
        
        return render(request, 'empleados/eliminar.html', {
            'empleado': empleado,
            'usuario_actual': request.session.get('username')
        })
    
    except DoesNotExist:
        return render(request, 'empleados/error.html', {'mensaje': 'Empleado no encontrado'})


# API Views para JSON responses
@csrf_exempt
@require_http_methods(["GET"])
def api_empleados(request):
    """API endpoint para obtener todos los empleados"""
    empleados = Empleado.objects.all()
    empleados_data = [empleado.to_dict() for empleado in empleados]
    return JsonResponse({'empleados': empleados_data})


@csrf_exempt
@require_http_methods(["GET"])
def api_empleado_detalle(request, empleado_id):
    """API endpoint para obtener un empleado específico"""
    try:
        empleado = Empleado.objects.get(id=empleado_id)
        return JsonResponse({'empleado': empleado.to_dict()})
    except DoesNotExist:
        return JsonResponse({'error': 'Empleado no encontrado'}, status=404)


@csrf_exempt
@require_http_methods(["POST"])
def api_crear_empleado(request):
    """API endpoint para crear un nuevo empleado"""
    try:
        data = json.loads(request.body)
        empleado = Empleado(
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            email=data.get('email'),
            telefono=data.get('telefono'),
            departamento=data.get('departamento'),
            cargo=data.get('cargo'),
            salario=float(data.get('salario', 0)),
            activo=data.get('activo', 'Si')
        )
        empleado.save()
        return JsonResponse({'empleado': empleado.to_dict()}, status=201)
    except (ValidationError, ValueError) as e:
        return JsonResponse({'error': str(e)}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def api_actualizar_empleado(request, empleado_id):
    """API endpoint para actualizar un empleado"""
    try:
        empleado = Empleado.objects.get(id=empleado_id)
        data = json.loads(request.body)
        
        empleado.nombre = data.get('nombre', empleado.nombre)
        empleado.apellido = data.get('apellido', empleado.apellido)
        empleado.email = data.get('email', empleado.email)
        empleado.telefono = data.get('telefono', empleado.telefono)
        empleado.departamento = data.get('departamento', empleado.departamento)
        empleado.cargo = data.get('cargo', empleado.cargo)
        empleado.salario = float(data.get('salario', empleado.salario))
        empleado.activo = data.get('activo', empleado.activo)
        empleado.save()
        
        return JsonResponse({'empleado': empleado.to_dict()})
    except DoesNotExist:
        return JsonResponse({'error': 'Empleado no encontrado'}, status=404)
    except (ValidationError, ValueError) as e:
        return JsonResponse({'error': str(e)}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def api_eliminar_empleado(request, empleado_id):
    """API endpoint para eliminar un empleado"""
    try:
        empleado = Empleado.objects.get(id=empleado_id)
        empleado.delete()
        return JsonResponse({'mensaje': 'Empleado eliminado correctamente'})
    except DoesNotExist:
        return JsonResponse({'error': 'Empleado no encontrado'}, status=404)
