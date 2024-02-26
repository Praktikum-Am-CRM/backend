from django.contrib import admin

from .models import (
    Ambassador,
    AmbassadorRequest,
    DeleviryStatus,
    DeliveryAddress,
    Merch,
    MerchRequest,
    Status,
)

admin.site.register(Ambassador)
admin.site.register(AmbassadorRequest)
admin.site.register(Merch)
admin.site.register(DeliveryAddress)
admin.site.register(MerchRequest)
admin.site.register(Status)
admin.site.register(DeleviryStatus)
