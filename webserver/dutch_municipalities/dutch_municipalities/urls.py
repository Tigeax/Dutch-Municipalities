from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import MunicipalityViewSet


router = DefaultRouter()
router.register(r'municipality', MunicipalityViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]