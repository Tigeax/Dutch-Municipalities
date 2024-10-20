from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_gis.filters import InBBoxFilter
from .models import Municipality
from .serializers import MunicipalitySerializer


class MunicipalityViewSet(ModelViewSet):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    filter_backends = (DjangoFilterBackend, InBBoxFilter)
    bbox_filter_field = "geometry"
