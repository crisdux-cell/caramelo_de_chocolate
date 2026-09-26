"""
Configuración de rutas (URLs) '.
Este archivo mapea las direcciones web (URLs) a las funciones de vistas (views) correspondientes.
"""
from django.urls import path
from . import views

urlpatterns = [
    # Autenticación
    path('', views.login_usuario, name='login_usuario'), 
    path('home/', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('jefe/registro-usuario/', views.registro_jefe, name='registro_jefe'),
    path('logout/', views.cerrar_sesion, name='logout'),

    # Proyectos
    path('crear/', views.crear_proyecto, name='crear_proyecto'),
    path('crear-modulo/<int:parent_id>/', views.crear_modulo, name='crear_modulo'),
    path('editar-proyecto/<int:pk>/', views.editar_proyecto, name='editar_proyecto'),
    path('eliminar/<int:pk>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('inhabilitar-proyecto/<int:pk>/', views.inhabilitar_proyecto, name='inhabilitar_proyecto'),
    path('proyectos-inhabilitados/', views.proyectos_inhabilitados, name='proyectos_inhabilitados'),
    path('restaurar-proyecto/<int:pk>/', views.restaurar_proyecto, name='restaurar_proyecto'),

    # Tareas (Gerente)
    path('asignar-tarea/<int:proyecto_id>/', views.asignar_tarea, name='asignar_tarea'),
    path('gestionar-asignaciones/<int:proyecto_id>/', views.gestionar_asignaciones, name='gestionar_asignaciones'),
    path('tareas-generales/', views.gestionar_tareas_generales, name='gestionar_tareas_generales'),
    
    # Equipos y Revisión (Gerente/Jefe)
    path('desarrolladores/', views.lista_devs, name='lista_desarrolladores'),
    path('gerentes/', views.lista_gerentes, name='lista_gerentes'),
    path('revision-tareas/', views.revision_tareas, name='revision_tareas'),
    path('aprobar-tarea/<int:pk>/', views.aprobar_tarea, name='aprobar_tarea'),
    path('devolver-tarea/<int:pk>/', views.devolver_tarea, name='devolver_tarea'),

    # Panel Desarrollador
    path('panel_desarrollador/<int:proyecto_id>/', views.panel_desarrollador, name='panel_desarrollador'),
    path('eliminar-tarea/<int:pk>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('tarea/<int:pk>/estado/<str:estado>/', views.cambiar_estado_tarea, name='cambiar_estado_tarea'),
    path('dev/crear-tarea/', views.dev_crear_tarea, name='dev_crear_tarea'),
    path('dev/editar-tarea/<int:pk>/', views.dev_editar_tarea, name='dev_editar_tarea'),
    path('tarea/<int:pk>/agregar-nota/', views.agregar_nota, name='agregar_nota'),
    path('nota/<int:pk>/eliminar/', views.eliminar_nota, name='eliminar_nota'),
    path('tarea/<int:pk>/registrar-tiempo/', views.registrar_tiempo, name='registrar_tiempo'),
    path('proyecto/<int:pk>/generar-reporte/', views.generar_reporte, name='generar_reporte'),
    path('gerente/crear-tarea/', views.gerente_crear_tarea, name='gerente_crear_tarea'),
    
    # Reportes
    path('reportes/', views.lista_reportes, name='lista_reportes'),
    path('reportes/<int:pk>/', views.ver_reporte, name='ver_reporte'),
]