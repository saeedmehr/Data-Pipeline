from rest_framework import serializers

from .models import Location, Reservation, NonrelLocation, NonrelReservation


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'wgs84_polygon']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'customer_id', 'start_latitude', 'start_longitude', 'srid', 'net_price']


class NonrelLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonrelLocation
        fields = ['id', 'wgs84_polygon']


class NonrelReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonrelReservation
        fields = ['id', 'customer_id', 'start_latitude', 'start_longitude', 'srid', 'net_price']
