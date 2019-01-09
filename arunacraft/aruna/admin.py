from django.contrib import admin

# Register your models here.

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


admin.site.register(Index_LinkerImage)
admin.site.register(Florarium_LinkerImage)
admin.site.register(Gift_LinkerImage)

admin.site.register(Goods_Florarium_EmptyForm)
admin.site.register(Goods_Florarium_FullForm)

admin.site.register(Goods_Gifts_ChristmasGift)
admin.site.register(Goods_Gifts_VitrazhPicture)
admin.site.register(Goods_Gifts_Souvenir)
admin.site.register(Goods_Gifts_Lamp)

admin.site.register(MasterClass)

