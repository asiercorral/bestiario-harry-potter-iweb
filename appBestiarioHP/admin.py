from django.contrib import admin
from .models import Criatura, Raza, Peligro

# Personalización del sitio de administración
admin.site.site_header = "Bestiario de Harry Potter - Administración"
admin.site.site_title = "Admin Bestiario HP"
admin.site.index_title = "Panel de Gestión del Bestiario"


@admin.register(Raza)
class RazaAdmin(admin.ModelAdmin):
    """Administración personalizada para el modelo Raza"""
    list_display = ('nombre', 'descripcion_corta')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
    
    def descripcion_corta(self, obj):
        """Muestra los primeros 50 caracteres de la descripción"""
        if obj.descripcion:
            return obj.descripcion[:50] + "..." if len(obj.descripcion) > 50 else obj.descripcion
        return "-"
    descripcion_corta.short_description = "Descripción"


@admin.register(Peligro)
class PeligroAdmin(admin.ModelAdmin):
    """Administración personalizada para el modelo Peligro (Clasificación del Ministerio)"""
    list_display = ('nombre', 'descripcion_corta')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
    
    def descripcion_corta(self, obj):
        """Muestra los primeros 50 caracteres de la descripción"""
        if obj.descripcion:
            return obj.descripcion[:50] + "..." if len(obj.descripcion) > 50 else obj.descripcion
        return "-"
    descripcion_corta.short_description = "Descripción"


@admin.register(Criatura)
class CriaturaAdmin(admin.ModelAdmin):
    """Administración personalizada para el modelo Criatura"""
    list_display = ('nombre', 'get_razas', 'categoria_peligro', 'tiene_imagen')
    list_filter = ('raza', 'categoria_peligro')
    search_fields = ('nombre', 'descripcion', 'donde_se_encuentra')
    ordering = ('nombre',)
    list_per_page = 20
    filter_horizontal = ('raza',)  # Widget mejorado para ManyToMany
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion')
        }),
        ('Clasificación', {
            'fields': ('raza', 'categoria_peligro'),
            'description': 'Seleccione la raza y nivel de peligro según el Ministerio de Magia'
        }),
        ('Detalles Adicionales', {
            'fields': ('caracteristicas', 'donde_se_encuentra'),
            'classes': ('collapse',),
            'description': 'Información adicional sobre la criatura'
        }),
    )
    
    def get_razas(self, obj):
        """Muestra las razas de la criatura"""
        return ", ".join([r.nombre for r in obj.raza.all()])
    get_razas.short_description = "Razas"
    
    def tiene_imagen(self, obj):
        """Indica si la criatura tiene imagen asociada"""
        if hasattr(obj, 'imagen'):
            return bool(obj.imagen)
        return False
    tiene_imagen.boolean = True
    tiene_imagen.short_description = "Imagen"