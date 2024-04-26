from django.urls import path
from . import views

app_name = "Clase"

urlpatterns = [
    path("", views.home, name="home"),
    path('agregar_curso/', views.agregar_curso, name='agregar_curso'),
    path('agregar_estudiante/', views.agregar_estudiante, name='agregar_estudiante'),
    path('agregar_profesor/', views.agregar_profesor, name='agregar_profesor'),
    path('agregar_comision/', views.agregar_comision, name='agregar_comision'),
]
