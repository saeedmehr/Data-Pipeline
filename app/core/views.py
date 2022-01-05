from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Location, Reservation, NonrelLocation, NonrelReservation
from core import serializers


class LocationList(APIView):
    def get(self, request, format=None):
        items = Location.objects.all()
        serializer = serializers.LocationSerializer(items, many=True)
        return Response(serializer.data)


class NonrelLocationList(APIView):
    def get(self, request, format=None):
        items = NonrelLocation.objects.all()
        serializer = serializers.NonrelLocationSerializer(items, many=True)
        return Response(serializer.data)


class ReservationList(APIView):
    def get(self, request, format=None):
        items = Reservation.objects.all()
        serializer = serializers.ReservationSerializer(items, many=True)
        return Response(serializer.data)


class NonrelReservationList(APIView):
    def get(self, request, format=None):
        items = NonrelReservation.objects.all()
        serializer = serializers.NonrelReservationSerializer(items, many=True)
        return Response(serializer.data)
