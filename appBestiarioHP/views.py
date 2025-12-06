from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import Criatura, Raza, Peligro


# =============================================================================
# VISTAS BASADAS EN CLASES (Class-Based Views)
# =============================================================================

# Vista de inicio (mantenemos como función por la lógica especial)
def index(request):
    razas = get_list_or_404(Raza.objects.order_by('nombre'))
    criaturas_usadas = set()
    lista = []
    for r in razas:
        criatura_repr = None
        for criatura in r.criatura_set.all():
            if criatura.id not in criaturas_usadas:
                criatura_repr = criatura
                criaturas_usadas.add(criatura.id)
                break
        lista.append({'raza': r, 'criatura': criatura_repr})
    context = {'lista_raza_criatura': lista}
    return render(request, 'index.html', context)


# Lista de criaturas - Vista basada en clase
class CriaturaListView(ListView):
    model = Criatura
    template_name = 'criaturas/lista.html'
    context_object_name = 'criaturas'
    ordering = ['nombre']


# Detalle de criatura - Vista basada en clase
class CriaturaDetailView(DetailView):
    model = Criatura
    template_name = 'criaturas/detalle.html'
    context_object_name = 'criatura'
    pk_url_kwarg = 'criatura_id'


# Lista de razas - Vista basada en clase
class RazaListView(ListView):
    model = Raza
    template_name = 'razas/lista.html'
    context_object_name = 'razas'
    ordering = ['nombre']


# Detalle de raza - Vista basada en clase
class RazaDetailView(DetailView):
    model = Raza
    template_name = 'razas/detalle.html'
    context_object_name = 'raza'
    pk_url_kwarg = 'raza_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['criaturas'] = self.object.criatura_set.all()
        return context


# Lista de peligros - Vista basada en clase
class PeligroListView(ListView):
    model = Peligro
    template_name = 'peligros/lista.html'
    context_object_name = 'peligros'
    ordering = ['nombre']


# Detalle de peligro - Vista basada en clase
class PeligroDetailView(DetailView):
    model = Peligro
    template_name = 'peligros/detalle.html'
    context_object_name = 'peligro'
    pk_url_kwarg = 'peligro_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['criaturas'] = self.object.criatura_set.all()
        return context


# =============================================================================
# API ENDPOINTS PARA AJAX
# =============================================================================

def api_criaturas(request):
    """API endpoint para obtener criaturas en formato JSON"""
    criaturas = Criatura.objects.all().order_by('nombre')
    data = []
    for c in criaturas:
        data.append({
            'id': c.id,
            'nombre': c.nombre,
            'descripcion': c.descripcion,
            'donde_se_encuentra': c.donde_se_encuentra,
            'categoria_peligro': c.categoria_peligro.nombre,
            'razas': [r.nombre for r in c.raza.all()]
        })
    return JsonResponse({'criaturas': data})


def api_buscar_criaturas(request):
    """API endpoint para buscar criaturas por nombre"""
    query = request.GET.get('q', '')
    criaturas = Criatura.objects.filter(nombre__icontains=query).order_by('nombre')
    data = []
    for c in criaturas:
        data.append({
            'id': c.id,
            'nombre': c.nombre,
            'descripcion': c.descripcion[:100] + '...' if len(c.descripcion) > 100 else c.descripcion,
            'categoria_peligro': c.categoria_peligro.nombre,
        })
    return JsonResponse({'criaturas': data, 'query': query})
