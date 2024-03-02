from django.contrib import admin

from .models import (
    Activity,
    Ambassador,
    AmbassadorActivity,
    AmbassadorGoal,
    AmbassadorStatus,
    AmbassadorStatusHistory,
    Goal,
)


@admin.register(Ambassador)
class AmbassadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'email', 'status')
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'status',
                    'promocode',
                    'receipt_date',
                    'reminder_counter',
                )
            },
        ),
        (
            'Персональная информация',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'middle_name',
                    'gender',
                    'birthday',
                )
            },
        ),
        ('Контакты', {'fields': ('email', 'phone', 'telegram_bot')}),
        (
            'Адрес',
            {
                'fields': (
                    'address_index',
                    'address_country',
                    'address_region',
                    'address_district',
                    'address_settlement',
                    'address_street',
                    'address_house',
                    'address_building',
                    'address_apartment',
                )
            },
        ),
        (
            'Дополнительная информация',
            {
                'fields': (
                    'blog_link',
                    'place_work',
                    'specialty_work',
                    'educational_institution',
                )
            },
        ),
    )

    def fio(self, object):
        return object.last_name + ' ' + object.first_name

    fio.short_description = 'ФИО'


@admin.register(AmbassadorGoal)
class AmbassadroGoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'ambassador', 'goal')


@admin.register(AmbassadorStatus)
class AmbassadorStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name', 'available')


@admin.register(AmbassadorStatusHistory)
class AmbassadorStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'ambassador', 'ambassador_status', 'assignment_date')


@admin.register(AmbassadorActivity)
class AmbassadorActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'ambassador', 'activity')


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'goal_name', 'available')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity_name', 'available')