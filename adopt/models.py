from django.db import models
from divulge.models import Pet
#from django.contrib.auth.models import User
from accounts.models import Users

class PedidoAdocao(models.Model):
    choices_status = (
        ('AG', 'Aguardando aprovação'),
        ('AP', 'Aprovado'),
        ('R', 'Recusado')
    )

    pet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    data = models.DateTimeField()
    status = models.CharField(max_length=2, choices=choices_status, default='AG')
    
    def __str__(self) -> str:
        return self.pet.nome