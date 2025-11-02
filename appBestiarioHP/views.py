from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Criatura, Raza, Peligro

# Portada: muestra una criatura por cada raza (la primera encontrada)
def index(request):
    razas = get_list_or_404(Raza.objects.order_by('nombre'))
    # Para pasar la criatura "representativa" a la plantilla,
    # construimos una lista de dicts {raza, criatura_representativa}
    lista = []
    for r in razas:
        criatura_repr = r.criatura_set.first()
        lista.append({'raza': r, 'criatura': criatura_repr})
    context = {'lista_raza_criatura': lista}
    return render(request, 'index.html', context)


# Lista de criaturas
def index_criaturas(request):
    criaturas = get_list_or_404(Criatura.objects.order_by('nombre'))
    context = {'criaturas': criaturas}
    return render(request, 'criaturas/lista.html', context)


# Detalle de criatura
def show_criatura(request, criatura_id):
    criatura = get_object_or_404(Criatura, pk=criatura_id)
    context = {'criatura': criatura}
    return render(request, 'criaturas/detalle.html', context)


# Lista de razas
def index_razas(request):
    razas = get_list_or_404(Raza.objects.order_by('nombre'))
    context = {'razas': razas}
    return render(request, 'razas/lista.html', context)


# Detalle de raza (incluye sus criaturas)
def show_raza(request, raza_id):
    raza = get_object_or_404(Raza, pk=raza_id)
    criaturas = raza.criatura_set.all()
    context = {'raza': raza, 'criaturas': criaturas}
    return render(request, 'razas/detalle.html', context)


# Lista de peligros (categorías)
def index_peligros(request):
    peligros = get_list_or_404(Peligro.objects.order_by('nombre'))
    context = {'peligros': peligros}
    return render(request, 'peligros/lista.html', context)


# Detalle de peligro (incluye sus criaturas)
def show_peligro(request, peligro_id):
    peligro = get_object_or_404(Peligro, pk=peligro_id)
    criaturas = peligro.criatura_set.all()
    context = {'peligro': peligro, 'criaturas': criaturas}
    return render(request, 'peligros/detalle.html', context)
