"""angeholly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
admin.autodiscover()

urlpatterns = [
    path('', include('apps.product.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.vendors.urls')),
    path('', include('apps.cart.urls')),
    path('', include('apps.shop.urls'))




]

urlpatterns += i18n_patterns(
    path('', include('apps.product.urls')),
    path('', include('apps.shop.urls')),

    path('', include('apps.vendors.urls')),
    path('', include('apps.cart.urls')),
    prefix_default_language=False,


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)