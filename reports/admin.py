from django.contrib import admin

from .models import Placement, Report, ReportStatus, ReportType


@admin.register(Placement)
class PlacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'site', 'available')


@admin.register(ReportStatus)
class ReportStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name', 'available')


@admin.register(ReportType)
class ReportTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name', 'available')


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ambassador',
        'report_type',
        'report_date',
        'content_link',
        'screen',
        'placement',
        'sign_junior',
        'report_status',
        'grade',
    )
