from django.urls import path
from . import views

urlpatterns = [
    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Web views
    path('', views.lista_empleados, name='lista_empleados'),
    path('detalle/<str:empleado_id>/', views.detalle_empleado, name='detalle_empleado'),
    path('crear/', views.crear_empleado, name='crear_empleado'),
    path('editar/<str:empleado_id>/', views.editar_empleado, name='editar_empleado'),
    path('eliminar/<str:empleado_id>/', views.eliminar_empleado, name='eliminar_empleado'),
    
    # API endpoints
    path('api/empleados/', views.api_empleados, name='api_empleados'),
    path('api/empleados/<str:empleado_id>/', views.api_empleado_detalle, name='api_empleado_detalle'),
    path('api/empleados/crear/', views.api_crear_empleado, name='api_crear_empleado'),
    path('api/empleados/actualizar/<str:empleado_id>/', views.api_actualizar_empleado, name='api_actualizar_empleado'),
    path('api/empleados/eliminar/<str:empleado_id>/', views.api_eliminar_empleado, name='api_eliminar_empleado'),
]
