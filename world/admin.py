from django.contrib.gis import admin
from world.models import Border, School, Facility, Busstop
from leaflet.admin import LeafletGeoAdmin


#admin.site.register(Border, admin.GeoModelAdmin)
#admin.site.register(School, admin.GeoModelAdmin)
#admin.site.register(Facility, admin.GeoModelAdmin)
#admin.site.register(Busstop, admin.GeoModelAdmin)

#admin.site.register(Border, admin.OSMGeoAdmin)
#admin.site.register(School, admin.OSMGeoAdmin)
#admin.site.register(Facility, admin.OSMGeoAdmin)
#admin.site.register(Busstop, admin.OSMGeoAdmin)

class BorderAdmin(LeafletGeoAdmin):
  search_fields = ['n03_001','n03_003','n03_004']
  list_filter = ('n03_003',)

admin.site.register(Border, BorderAdmin)
admin.site.register(School, LeafletGeoAdmin)
admin.site.register(Facility, LeafletGeoAdmin)
admin.site.register(Busstop, LeafletGeoAdmin)
