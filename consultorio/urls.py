from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('eliminar_paciente/<int:id>/', views.eliminar_paciente),
    path('eliminar_cita/<int:id>/', views.eliminar_cita),
    path('editar_paciente/<int:id>/',views.editar_paciente,name='editar_paciente'),
    path('editar_cita/<int:id>/',views.editar_cita,name='editar_cita'),

]