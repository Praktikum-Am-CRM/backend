from django.contrib import admin

from .models import Placement, Report, ReportStatus, ReportType

admin.site.register(Placement)
admin.site.register(ReportStatus)
admin.site.register(ReportType)
admin.site.register(Report)

# class PostAdmin(admin.ModelAdmin):
#     list_display = (
#         'pk',
#         'text',
#         'pub_date',
#         'author',
#         'group'
#     )
#     # Интерфейс для поиска по тексту постов
#     search_fields = ('text',)
#     # Возможность менять поле group в любом посте
#     list_editable = ('group',)
#     # Возможность фильтрации по дате
#     list_filter = ('pub_date',)
#     # Свойство для пустых полей по-умолчанию
#     empty_value_display = '-пусто-'