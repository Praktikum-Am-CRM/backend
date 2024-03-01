from django.contrib import admin

from .models import (
    AmbassadorRequest,
    DeliveryAddress,
    DeliveryHistory,
    DeliveryStatus,
    Merch,
    MerchRequest,
)


@admin.register(AmbassadorRequest)
class AmbassadorRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'ambassador', 'merch_request', 'assignment_date')


@admin.register(Merch)
class MerchAdmin(admin.ModelAdmin):
    list_display = ('id', 'merch_name', 'price', 'intangible', 'available')


@admin.register(DeliveryAddress)
class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_confirmed', 'address')
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'index',
                    'country',
                    'region',
                    'settlement',
                    'district',
                    'street',
                    'house',
                    'building',
                    'apartment',
                )
            },
        ),
    )

    def address(self, object):
        if object:
            return str(object)
        return ''

    address.description = 'Адрес доставки'


@admin.register(MerchRequest)
class MerchRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'manager',
        'merch',
        'delivery_address',
        'request_status',
    )


@admin.register(DeliveryStatus)
class DeliveryStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name', 'available')


@admin.register(DeliveryHistory)
class DeliveryHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'merch_request',
        'delivery_status',
        'assignment_date',
    )
