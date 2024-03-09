from django.contrib import admin

from crm_settings.models import CrmSettings


@admin.register(CrmSettings)
class CrmSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'default_ambassador_status',
        'default_message_type',
        'default_message_status',
        'delayed_sending_message_type',
        'default_delivery_status',
        'default_report_status',
        'default_report_type'
    )
