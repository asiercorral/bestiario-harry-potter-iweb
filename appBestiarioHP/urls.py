from django.urls import path
from . import views
from .views import (
    CriaturaListView, CriaturaDetailView,
    RazaListView, RazaDetailView,
    PeligroListView, PeligroDetailView
)

urlpatterns = [
    path('', views.index, name='index'),

    # Criaturas (vistas basadas en clases)
    path('criaturas/', CriaturaListView.as_view(), name='criaturas'),
    path('criaturas/<int:criatura_id>/', CriaturaDetailView.as_view(), name='detalle_criatura'),

    # Razas (vistas basadas en clases)
    path('razas/', RazaListView.as_view(), name='razas'),
    path('razas/<int:raza_id>/', RazaDetailView.as_view(), name='detalle_raza'),

    # Categorías de peligro (vistas basadas en clases)
    path('peligros/', PeligroListView.as_view(), name='peligros'),
    path('peligros/<int:peligro_id>/', PeligroDetailView.as_view(), name='detalle_peligro'),

    # API para búsqueda AJAX
    path('api/buscar-criaturas/', views.api_buscar_criaturas, name='api_buscar_criaturas'),
    path('api/buscar-razas/', views.api_buscar_razas, name='api_buscar_razas'),
]
