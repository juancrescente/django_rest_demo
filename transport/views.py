from rest_framework import generics, status
from transport.models import Provider, ServiceArea
from transport.serializers import ProviderSerializer, ServiceAreaSerializer
from django.contrib.gis.geos import Point
from rest_framework.response import Response
import json


class ProviderListCreate(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaList(generics.ListCreateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaQuery(generics.ListAPIView):
    serializer_class = ServiceAreaSerializer

    def get(self, request, *args, **kwargs):
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
        point = Point(float(lat), float(lng))
        items = ServiceArea.objects.filter(poly__intersects=point)
        serializer = ServiceAreaSerializer(items, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        pass
