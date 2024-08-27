from django.urls import path
from app2 import views

urlpatterns = [
    path('index2/', views.index2),
    path('saludo/', views.saludo),
    path('text2/', views.testeo2),
    path('pagina2/', views.pag2),
    ]