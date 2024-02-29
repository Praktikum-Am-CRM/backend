from django.contrib import admin

from .models import (
    AmbassadorRequest,
    DeliveryAddress,
    DeliveryStatus,
    Merch,
    MerchRequest,
)

admin.site.register(AmbassadorRequest)
admin.site.register(Merch)
admin.site.register(DeliveryAddress)
admin.site.register(MerchRequest)
admin.site.register(DeliveryStatus)
