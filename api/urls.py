from django.urls import include, path
from djoser import views
from djoser.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.view_ambassadors import AmbassadorViewSet
from api.view_utilities import (
    get_achievies,
    get_activities,
    get_ambassador_statuses,
    get_delivery_statuses,
    get_goals,
    get_message_statuses,
    get_message_types,
    get_placements,
    get_pool_messages,
    get_programs,
    get_report_statuses,
    get_report_types,
)
from api.views_program import AmbassadorProgramViewsList
from api.views_status import AmbassadorStatusViewSet

from .view_telegram import TelegramUserCreateView
from .views_botmessage import BotMessagesViewSet
from .views_merches import MerchesViewSet
from .views_reports import ReportViewSet

app_name = 'api'

router = DefaultRouter()
router.register('ambassador', AmbassadorViewSet, basename='ambassador')
router.register(
    'telegram_user', TelegramUserCreateView, basename='telegram_user_create'
)
router.register(r'report', ReportViewSet, basename='report')
router.register('merch_request', MerchesViewSet, basename='merch_request')
router.register(
    'statistic/ambassador_program',
    AmbassadorProgramViewsList,
    basename='ambassador_program',
)
router.register(
    'statistic/ambassador_status',
    AmbassadorStatusViewSet,
    basename='ambassador_status',
)
router.register('bot_message', BotMessagesViewSet, basename='bot_message')

decorated_login_view = swagger_auto_schema(
    method='POST',
    operation_id='Obtain user authentication token',
    permission_classes=(permissions.AllowAny,),
    tags=['Пользователи'],
    responses={
        200: settings.SERIALIZERS.token,
        400: 'Не верные данные для авторизации',
    },
)(views.TokenCreateView.as_view())

decorated_logout_view = swagger_auto_schema(
    method='POST',
    operation_id='Remove user authentication token',
    permission_classes=(permissions.AllowAny,),
    tags=['Пользователи'],
    responses={204: 'Успешно', 401: 'Не авторизированный пользователь'},
)(views.TokenDestroyView.as_view())

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/login', decorated_login_view, name='login'),
    path('auth/token/logout', decorated_logout_view, name='logout'),
    path(
        'utility/report_types',
        get_report_types,
        name='get_report_types',
    ),
    path(
        'utility/report_statuses',
        get_report_statuses,
        name='get_report_statuses',
    ),
    path('utility/placements', get_placements, name='get_placements'),
    path('utility/goals', get_goals, name='get_goals'),
    path('utility/activities', get_activities, name='get_activities'),
    path(
        'utility/ambassador_statuses',
        get_ambassador_statuses,
        name='get_ambassador_statuses',
    ),
    path('utility/achievies', get_achievies, name='get_achivies'),
    path(
        'utility/pool_messages',
        get_pool_messages,
        name='get_pool_messages',
    ),
    path(
        'utility/message_statuses',
        get_message_statuses,
        name='get_message_statuses',
    ),
    path(
        'utility/message_types',
        get_message_types,
        name='get_message_types',
    ),
    path(
        'utility/delivery_statuses',
        get_delivery_statuses,
        name='get_delivery_statuses',
    ),
    path('utility/programs', get_programs, name='programs'),
]
