from django.contrib import admin

from ambassador.models import AmbassadorProgram

from .models import Program


@admin.register(Program)
class AchieveAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'program_name',
        'available',
    )


@admin.register(AmbassadorProgram)
class AmbassadorAchieveAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ambassador',
        'program',
    )
