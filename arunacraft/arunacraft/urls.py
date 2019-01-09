"""arunacraft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from aruna import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    # path('index/', views.index, name='index'),
    path('florarium.html', views.florarium, name='florarium'),
    # path('florarium/', views.florarium, name='florarium'),
    path('empty.html', views.florarium_empty, name='florarium_empty'),
    # path('florarium/empty/', views.florarium_empty, name='florarium_empty'),
    path('full.html', views.florarium_full, name='florarium_full'),
    # path('florarium/full/', views.florarium_full, name='florarium_full'),
    path('decor.html', views.gifts, name='gifts_decor'),
    # path('gifts/', views.gifts, name='gifts_decor'),
    path('toys.html', views.gifts_christmasToys, name='gifts_toys'),
    # path('gifts/toys/', views.gifts_christmasToys, name='gifts_toys'),
    path('vpictures.html', views.gifts_vpictures, name='gifts_vpictures'),
    # path('gifts/vpictures/', views.gifts_vpictures, name='gifts_vpictures'),
    path('souvenirs.html', views.gifts_souvenirs, name='gifts_souvenirs'),
    # path('gifts/souvenirs/', views.gifts_souvenirs, name='gifts_souvenirs'),
    path('light.html', views.gifts_lamp, name='gifts_lightlamp'),
    # path('gifts/light/', views.gifts_lamp, name='gifts_lightlamp'),
    path('contacts.html', views.contacts, name='contacts'),
    # path('gifts/contacts/', views.contacts, name='contacts'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
