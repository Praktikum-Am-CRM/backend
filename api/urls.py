from django.urls import include, path
from djoser import views
from djoser.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

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
        400: 'Не верные данные для авторизации'
    }
)(views.TokenCreateView.as_view())

decorated_logout_view = swagger_auto_schema(
    method='POST',
    operation_id='Remove user authentication token',
    permission_classes=(permissions.AllowAny,),
    tags=['Пользователи'],
    responses={
        204: 'Успешно',
        401: 'Не авторизированный пользователь'
    }
)(views.TokenDestroyView.as_view())

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/login', decorated_login_view, name='login'),
    path('auth/token/logout', decorated_logout_view, name='logout'),
]
