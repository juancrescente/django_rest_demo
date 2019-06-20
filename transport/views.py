from rest_framework import generics, status
from transport.models import Provider, ServiceArea
from transport.serializers import ProviderSerializer, ServiceAreaSerializer
from django.contrib.gis.geos import Point
from rest_framework.response import Response
import json
from rest_framework.permissions import IsAuthenticated


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
        point = Point(float(lng), float(lat))
        items = ServiceArea.objects.filter(poly__intersects=point)
        serializer = ServiceAreaSerializer(items, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        pass
