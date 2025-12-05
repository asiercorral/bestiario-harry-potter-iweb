from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Criaturas
    path('criaturas/', views.index_criaturas, name='criaturas'),
    path('criaturas/<int:criatura_id>/', views.show_criatura, name='detalle_criatura'),

    # Razas
    path('razas/', views.index_razas, name='razas'),
    path('razas/<int:raza_id>/', views.show_raza, name='detalle_raza'),

    # Categorías de peligro
    path('peligros/', views.index_peligros, name='peligros'),
    path('peligros/<int:peligro_id>/', views.show_peligro, name='detalle_peligro'),

    # Agenda
    path('agenda/', views.agenda, name='agenda'),
]
