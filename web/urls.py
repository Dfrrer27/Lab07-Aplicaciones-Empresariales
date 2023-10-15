from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.AlumnoView.as_view(), name='index'),
    path('eliminar/<int:alumno_id>/', views.BorrarView.as_view(), name='eliminar_alumno'),
    path('profesor/', views.ProfesorView.as_view(), name='profesor'),
    path('profesor/eliminar/<int:profesor_id>/', views.ProfesorDeleteView.as_view(), name='eliminar_profesor'),
]
