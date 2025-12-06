"""
URL configuration for bestiarioHP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

# URLs sin prefijo de idioma
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Para cambiar idioma
]

# URLs con prefijo de idioma (ej: /es/, /en/)
urlpatterns += i18n_patterns(
    path('', include('appBestiarioHP.urls')),  # redirige a la app
    path('admin/', admin.site.urls),
    prefix_default_language=False,  # No añade prefijo para el idioma por defecto (es)
)
