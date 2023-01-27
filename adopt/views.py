from django.http import HttpResponse
from django.shortcuts import render, redirect
from divulge.models import Pet, Raca
from django.contrib import messages
from django.contrib.messages import constants
from .models import PedidoAdocao
from datetime import datetime
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def listar_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status='P')
        racas = Raca.objects.all()
        
        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')
        
        if cidade:
            pets = pets.filter(cidade__icontains=cidade)
        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)
            raca_filter = Raca.objects.get(id=raca_filter)
        
        return render(request, 'adopt/listar_pets.html',{'pets':pets, 'racas':racas, 'cidade':cidade, 'raca_filter':raca_filter})

def pedido_adocao(request,id_pet):
    pet = Pet.objects.filter(id=id_pet).filter(status="P")
    
    if not pet.exists():
        messages.add_message(request, constants.WARNING, 'Esse pet já foi adotado')
        return redirect('/adotar')
    
    pedido = PedidoAdocao(pet=pet.first(),
                          usuario=request.user,
                          data=datetime.now())
    pedido.save()
    messages.add_message(request, constants.SUCCESS, 'Pedido de adoçao realizado com suesso')
    return redirect('/adotar')

def processa_pedido_adocao(request, id_pedido):
    status = request.GET.get('status')
    pedido = PedidoAdocao.objects.get(id=id_pedido)
    pet = Pet.objects.get(id=pedido.pet_id) # type: ignore    
    if status == 'A':
        pedido.status = 'AP'
        pet.status = 'A'
        string = '''Olá sua adoção foi aprovada com sucesso'''
    elif status == 'R':
        string = '''Olá sua adoção foi recusada'''
        pedido.status = 'R'
        
    pedido.save()
    pet.save()
    html_content = render_to_string('emails/adocao_confirmada.html',{'string':string, 'pedido':pedido, 'pet':pet, 'status':status})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives('Seu pedido de adoçao foi Processado', text_content, settings.EMAIL_HOST_USER,[pedido.usuario.email,])
    email.attach_alternative(html_content, 'text/html')
    email.send()
    # email = send_mail(
    #     'Sua adoção foi processada',
    #     string,#type:ignore
    #     'vinicios471matheus@outlook.com',
    #     [pedido.usuario.email,],
    # )
    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção processado com sucesso')
    return redirect('/divulgar/ver_pedido_adocao')
  