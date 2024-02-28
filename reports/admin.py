from django.contrib import admin

from .models import Placement, Report, ReportStatus, ReportType

admin.site.register(Placement)
admin.site.register(ReportStatus)
admin.site.register(ReportType)
admin.site.register(Report)
