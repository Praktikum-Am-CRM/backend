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


admin.site.register(AmbassadorGoal)
admin.site.register(AmbassadorStatus)
admin.site.register(AmbassadorStatusHistory)
admin.site.register(AmbassadorActivity)
admin.site.register(Goal)
admin.site.register(Activity)
