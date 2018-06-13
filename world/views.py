from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter
from rest_framework.pagination import PageNumberPagination

from .serializers import BorderSerializer, SchoolSerializer, FacilitySerializer, BusstopSerializer
from .models import Border, School, Facility, Busstop


class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

class BorderViewSet(viewsets.ModelViewSet):
    queryset = Border.objects.all()
    serializer_class = BorderSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True


class BusstopViewSet(viewsets.ModelViewSet):
    queryset = Busstop.objects.all()
    serializer_class = BusstopSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter, InBBoxFilter)
    distance_filter_field = bbox_filter_field = 'geom'
    distance_filter_convert_meters = True
