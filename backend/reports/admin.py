from django.contrib import admin
from .models import Placement, RunStatus, TypeReport, Report

admin.site.register(Placement)
admin.site.register(RunStatus)
admin.site.register(TypeReport)
admin.site.register(Report)
