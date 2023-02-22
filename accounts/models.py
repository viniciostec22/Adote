from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    foto_perfil = models.ImageField(upload_to='fotos_perfil')
    telefone = models.CharField(max_length=14, default='',blank=True)
