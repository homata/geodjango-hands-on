from rest_framework import serializers
from world.models import Border, School, Facility, Busstop

class BorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Border
        fields = ('__all__')
        #exclude = ('n03_001', 'n03_002')
