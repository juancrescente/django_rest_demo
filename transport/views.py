from rest_framework import generics, status
from transport.models import Provider, ServiceArea
from transport.serializers import ProviderSerializer, ServiceAreaSerializer
from django.contrib.gis.geos import Point
from rest_framework.response import Response
import json
from django.conf import settings
#from rest_framework.permissions import IsAuthenticated
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

class ProviderListCreate(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaList(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaQuery(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    serializer_class = ServiceAreaSerializer


    def get(self, request, *args, **kwargs):
        CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
        lat = self.request.query_params.get('lat', 'a')
        lng = self.request.query_params.get('lng', 'a')
        try:
            lat = float(lat)
        except ValueError:
            res = {"code": 400, "message": "lat parameter is not valid"}
            return Response(data=json.dumps(res), status=status.HTTP_400_BAD_REQUEST)
        try:
            lng = float(lng)
        except ValueError:
            res = {"code": 400, "message": "lng parameter is not valid"}
            return Response(data=json.dumps(res), status=status.HTTP_400_BAD_REQUEST)
        key = "%s_%s" % (lat, lng)
 #       if key in cache:
#            serialized = cache.get(key)
#            return Response(serialized)
        point = Point(float(lng), float(lat))
        items = ServiceArea.objects.filter(poly__intersects=point)
        serializer = ServiceAreaSerializer(items, many=True)
        cache.set(key, serializer.data, timeout=CACHE_TTL)
        return Response(serializer.data)

    def get_queryset(self):
        pass
