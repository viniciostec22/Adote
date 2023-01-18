from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from adopt.models import PedidoAdocao
from .models import Tag, Raca, Pet
from django.contrib import messages
from django.contrib.messages import constants
from accounts.models import Users
from django.views.decorators.csrf import csrf_exempt

@login_required # type: ignore
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
        if len(nome.strip()) == 0 or len(descricao.strip()) == 0 or len(estado.strip()) == 0 or len(cidade.strip()) == 0 or len(telefone.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'há Campos obrigatorios em branco')
            return render(request, 'divulge/novo_pet.html')
       
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
        
@login_required  # type: ignore      
def seus_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.filter(usuario = request.user)
        return render(request, 'divulge/seus_pets.html',{'pets':pets})
   
@login_required  
def remover_pet(request, id):
    pet = Pet.objects.get(id=id)
    
    if not pet.usuario == request.user:
        messages.add_message(request, constants.ERROR, 'Esse Pet não é seu')
        return redirect('/divulgar/seus_pets')
    pet.delete()
    messages.add_message(request, constants.SUCCESS, 'Pet removido com sucesso')
    return redirect('/divulgar/seus_pets')

@login_required 
def ver_pet(request, id):
    if request.method == 'GET':
        pet = Pet.objects.get(id=id)
        return render(request, 'divulge/ver_pet.html', {'pet':pet})
@login_required   
def ver_pedido_adocao(request):
    if request.method == 'GET':
        
        pedidos = PedidoAdocao.objects.filter(pet__usuario=request.user).filter(status='AG').filter(pet__status='P')
        return  render(request, 'divulge/ver_pedido_adocao.html', {'pedidos':pedidos})

@login_required    
def dashboard(request):
    if request.method == 'GET':
        return render(request, 'divulge/dashboard.html')

@login_required 
@csrf_exempt
def api_adocoes_por_raca(request):
    racas = Raca.objects.all()
    qtd_adocoes = []
    for raca in racas:
        adocoes = PedidoAdocao.objects.filter(pet__raca=raca).filter(status='AP').count()
        qtd_adocoes.append(adocoes)
        
    racas = [raca.raca for raca in racas]
    data = {'qtd_adocoes': qtd_adocoes,
            'labels':racas}
    return JsonResponse(data)