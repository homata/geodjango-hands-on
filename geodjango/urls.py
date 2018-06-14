"""geodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.gis import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from world.views import BorderViewSet, SchoolViewSet, FacilityViewSet, BusstopViewSet
from world.views import index, GeojsonAPIView
from django.views.generic.base import RedirectView

router = DefaultRouter()
router.register('border', BorderViewSet)
router.register('school', SchoolViewSet)
router.register('facility', FacilityViewSet)
router.register('busstop', BusstopViewSet)

urlpatterns = [
    path('favicon\.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('api/', include(router.urls)),
    path('', index, name='world_index'),
    path('world/geojson/', GeojsonAPIView.as_view(), name='geojson_view'),
]
