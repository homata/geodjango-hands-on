from rest_framework import serializers
from .models import Border, School, Facility, Busstop

# 札幌市, 半径100m
# http://127.0.0.1:8000/api/border/?dist=300&point=141.354389,43.062083
# http://127.0.0.1:8000/api/school/?dist=100&point=140.9278,41.9582
# http://127.0.0.1:8000/api/facility/?dist=100&point=140.9278,41.9582
# http://127.0.0.1:8000/api/busstop/?dist=1000&point=140.97150344,41.90632327
# http://127.0.0.1:8000/api/busstop/?page_size=10&page=1
# http://localhost:8000/api/places/?in_bbox=135.48,34.6969,135.4984,34.7055

class BorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Border
        fields = ('__all__')

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('__all__')

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ('__all__')

class BusstopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Busstop
        exclude = ("p11_003_2", "p11_003_3", "p11_003_4", "p11_003_5", "p11_003_6", "p11_003_7", "p11_003_8", "p11_003_9",
                   "p11_003_10", "p11_003_11", "p11_003_12", "p11_003_13", "p11_003_14", "p11_003_15",
                   "p11_003_16", "p11_003_17", "p11_003_18", "p11_003_19",
                   "p11_004_2", "p11_004_3", "p11_004_4", "p11_004_5", "p11_004_6", "p11_004_7", "p11_004_8", "p11_004_9",
                   "p11_004_10", "p11_004_11", "p11_004_12", "p11_004_13", "p11_004_14", "p11_004_15", "p11_004_16",
                   "p11_004_17", "p11_004_18", "p11_004_19")
