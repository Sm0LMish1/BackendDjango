from django.urls import path
from app1 import views

urlpatterns = [
    path('inicio/', views.index),
    path('text/', views.testeo1),
    path('pagina1/', views.pag1),
    ]
