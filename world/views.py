from rest_framework import viewsets
from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter
from rest_framework.pagination import PageNumberPagination

from .serializers import BorderSerializer, SchoolSerializer, FacilitySerializer, BusstopSerializer
from .models import Border, School, Facility, Busstop

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import traceback
import json
from django.core.serializers import serialize

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Django REST Frameworkに再挑戦 その5
#   http://pythonskywalker.hatenablog.com/entry/2017/01/05/172222
# Django REST frameworkでAPIにアクセス権を実装する方法
#   http://racchai.hatenablog.com/entry/2016/05/27/070000
from rest_framework.permissions import IsAuthenticated

# -----------------------------------------
@login_required
def index(request):
    """
    index()
    """

    contexts = {}

    # 現在ログインしている?
    if request.user.is_authenticated:
        contexts['user'] = {"username": request.user.username, "user_id": request.user.id, "is_authenticated": True}

    return render(request,'world/index.html',contexts)

# -----------------------------------------
class GeojsonAPIView(APIView):
    """
    GeoJsonデータ取得
    @return geojson形式
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **keywords):
        try:
            # "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
            #encjson  = serialize('geojson', Border.objects.filter(n03_003="札幌市"),srid=4326, geometry_field='geom', fields=('n03_004',) )
            encjson  = serialize('geojson', Border.objects.filter(n03_004="中央区"),srid=4326, geometry_field='geom', fields=('n03_003','n03_004',) )
            result   = json.loads(encjson)
            response = Response(result, status=status.HTTP_200_OK)

        except Exception as e:
            traceback.print_exc()
            response = Response({}, status=status.HTTP_404_NOT_FOUND)

        except:
            response = Response({}, status=status.HTTP_404_NOT_FOUND)

        return response

# -----------------------------------------
class MyPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

# -----------------------------------------
class BorderViewSet(viewsets.ModelViewSet):
    queryset = Border.objects.all()
    serializer_class = BorderSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True

# -----------------------------------------
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True

# -----------------------------------------
class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter,)
    distance_filter_field = 'geom'
    distance_filter_convert_meters = True

# -----------------------------------------
class BusstopViewSet(viewsets.ModelViewSet):
    queryset = Busstop.objects.all()
    serializer_class = BusstopSerializer
    pagination_class = MyPagination
    filter_backends = (DistanceToPointFilter, InBBoxFilter)
    distance_filter_field = bbox_filter_field = 'geom'
    distance_filter_convert_meters = True


