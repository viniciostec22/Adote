from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Tag, Raca, Pet
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.
@login_required
def novo_pet(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        racas = Raca.objects.all()
        return render(request, 'divulge/novo_pet.html',{'tags':tags, 'racas':racas})
    elif request.method =='POST':
        foto = request.FILES.get('foto')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        tags = request.POST.getlist('tags')
        raca = request.POST.get('raca')
        #TODO: validar os dados 
        
        pet = Pet(
            usuario=request.user,
            foto=foto,
            nome=nome,
            descricao=descricao,
            estado=estado,
            cidade=cidade,
            telefone=telefone,
            raca_id=raca,
        )
        pet.save()
        
        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            pet.tags.add(tag)
        pet.save()
        messages.add_message(request, constants.SUCCESS, 'Pet Cadastrado com sucesso')
        return redirect('/divulgar/seus_pets')
        #TODO: mensagens de erros  
@login_required        
def seus_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.filter(usuario = request.user)
        return render(request, 'divulge/seus_pets.html',{'pets':pets})
    
def remover_pet(request, id):
    pet = Pet.objects.get(id=id)
    
    if not pet.usuario == request.user:
        messages.add_message(request, constants.ERROR, 'Esse Pet não é seu')
        return redirect('/divulgar/seus_pets')
    pet.delete()
    messages.add_message(request, constants.SUCCESS, 'Pet removido com sucesso')
    return redirect('/divulgar/seus_pets')