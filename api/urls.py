from django.urls import include, path
from djoser import views
from djoser.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.view_utilities import (
    get_achivies,
    get_activities,
    get_ambassador_statuses,
    get_delivery_statuses,
    get_goals,
    get_message_statuses,
    get_message_types,
    get_placements,
    get_pool_messages,
    get_report_statuses,
    get_report_types,
)

app_name = 'api'

router = DefaultRouter()
# router.register('my_data', GetMethod, basename='my_data')

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
        'api/v1/utility/report_types',
        get_report_types,
        name='get_report_types'
    ),
    path(
        'api/v1/utility/report_statuses',
        get_report_statuses,
        name='get_report_statuses'
    ),
    path(
        'api/v1/utility/placements',
        get_placements,
        name='get_placements'
    ),
    path(
        'api/v1/utility/goals',
        get_goals,
        name='get_goals'
    ),
    path(
        'api/v1/utility/activities',
        get_activities,
        name='get_activities'
    ),
    path(
        'api/v1/utility/ambassador_statuses',
        get_ambassador_statuses,
        name='get_ambassador_statuses'
    ),
    path(
        'api/v1/utility/achivies',
        get_achivies,
        name='get_achivies'
    ),
    path(
        'api/v1/utility/pool_messages',
        get_pool_messages,
        name='get_pool_messages'
    ),
    path(
        'api/v1/utility/message_statuses',
        get_message_statuses,
        name='get_message_statuses'
    ),
    path(
        'api/v1/utility/message_types',
        get_message_types,
        name='get_message_types'
    ),
    path(
        'api/v1/utility/delivery_statuses',
        get_delivery_statuses,
        name='get_delivery_statuses'
    ),
]
