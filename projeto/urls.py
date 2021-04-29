from django.urls import path
from . import views

urlpatterns = [
   
    path('projeto/',views.projeto, name='projeto'),
]