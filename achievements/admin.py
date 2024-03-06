from django.contrib import admin

from ambassador.models import AmbassadorAchieve

from .models import Achieve


@admin.register(Achieve)
class AchieveAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'achieve_name',
        'available',
    )


@admin.register(AmbassadorAchieve)
class AmbassadorAchieveAdmin(admin.ModelAdmin):
    list_display = ('id', 'ambassador', 'achieve', 'assignment_date')
