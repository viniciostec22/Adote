from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.logar, name='login'),
    path('sair/', views.sair, name="sair"),
    path('editar_user/<int:id>', views.editar_user, name='editar_usuario')
]
