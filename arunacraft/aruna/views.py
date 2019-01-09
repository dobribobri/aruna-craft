from django.shortcuts import render

# Create your views here.

from .models import Index_LinkerImage
from .models import Florarium_LinkerImage
from .models import Gift_LinkerImage

from .models import Goods_Florarium_EmptyForm
from .models import Goods_Florarium_FullForm

from .models import Goods_Gifts_ChristmasGift
from .models import Goods_Gifts_VitrazhPicture
from .models import Goods_Gifts_Souvenir
from .models import Goods_Gifts_Lamp

from .models import MasterClass

from django.conf import settings

import os

# Create your views here.


def index(request):
    linkers = Index_LinkerImage.objects.all()
    linker1, linker2, linker3 = None, None, None
    if len(linkers) > 0: linker1 = linkers[0]
    if len(linkers) > 1: linker2 = linkers[1]
    if len(linkers) > 2: linker3 = linkers[2]
    return render(request, 'index.html', {'linker1': linker1,
                                          'linker2': linker2,
                                          'linker3': linker3})


def florarium(request):
    linkers = Florarium_LinkerImage.objects.all()
    linker1, linker2, linker3 = None, None, None
    if len(linkers) > 0: linker1 = linkers[0]
    if len(linkers) > 1: linker2 = linkers[1]
    if len(linkers) > 2: linker3 = linkers[2]
    return render(request, 'florarium.html', {'linker1': linker1,
                                              'linker2': linker2,
                                              'linker3': linker3})


def gifts(request):
    linkers = Gift_LinkerImage.objects.all()
    linker1, linker2, linker3 = None, None, None
    if len(linkers) > 0: linker1 = linkers[0]
    if len(linkers) > 1: linker2 = linkers[1]
    if len(linkers) > 2: linker3 = linkers[2]
    return render(request, 'decor.html', {'linker1': linker1,
                                          'linker2': linker2,
                                          'linker3': linker3})


def florarium_empty(request):
    goods = Goods_Florarium_EmptyForm.objects.all()
    return render(request, 'empty.html', {'goods': goods})


def florarium_full(request):
    goods = Goods_Florarium_FullForm.objects.all()
    return render(request, 'full.html', {'goods': goods})


def gifts_christmasToys(request):
    goods = Goods_Gifts_ChristmasGift.objects.all()
    return render(request, 'toys.html', {'goods': goods})


def gifts_vpictures(request):
    goods = Goods_Gifts_VitrazhPicture.objects.all()
    return render(request, 'vpictures.html', {'goods': goods})


def gifts_souvenirs(request):
    goods = Goods_Gifts_Souvenir.objects.all()
    return render(request, 'souvenirs.html', {'goods': goods})


def gifts_lamp(request):
    goods = Goods_Gifts_Lamp.objects.all()
    return render(request, 'light.html', {'goods': goods})


def contacts(request):
    return render(request, 'contacts.html')
    
    