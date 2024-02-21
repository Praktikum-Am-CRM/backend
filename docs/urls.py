from rest_framework.routers import DefaultRouter

app_name = 'docs'

router = DefaultRouter()
# router.register('my_data', GetMethod, basename='my_data')
urlpatterns = router.urls
