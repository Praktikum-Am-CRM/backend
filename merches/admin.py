from django.contrib import admin

from .models import (Ambassador, RequestAmbassador,
                     Merch, DeliveryAddress, Request)

admin.site.register(Ambassador)
admin.site.register(RequestAmbassador)
admin.site.register(Merch)
admin.site.register(DeliveryAddress)
admin.site.register(Request)
