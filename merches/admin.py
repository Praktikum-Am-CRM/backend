from django.contrib import admin

from .models import (
    Ambassador,
    DeliveryAddress,
    Merch,
    Request,
    RequestAmbassador,
    Status,
)

admin.site.register(Ambassador)
admin.site.register(RequestAmbassador)
admin.site.register(Merch)
admin.site.register(DeliveryAddress)
admin.site.register(Request)
admin.site.register(Status)
