from django.contrib import admin

from .models import AmbassadorProgram, Program


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
