from django.shortcuts import render
from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework import generics,viewsets
from world import models, serializers
from rest_framework.pagination import PageNumberPagination

class BorderViewSet(viewsets.ModelViewSet):
    queryset = models.Border.objects.all()
    serializer_class = serializers.BorderSerializer
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True
