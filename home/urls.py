
from home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('quienes-somos/', views.quienesSomos, name='quienes-somos'),
    path('contacto/', views.contacto, name='contacto'),
]
