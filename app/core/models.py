from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry, Point

from djongo import models as djongo_models


class Reservation(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    start_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    start_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    srid = models.CharField(max_length=10)
    net_price = models.IntegerField()
    the_geom = models.PointField()

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.the_geom = Point(
            x=float(self.start_longitude),
            y=float(self.start_latitude),
            srid=int(self.srid),
        ) if self.start_longitude else None

        super(Reservation, self).save(*args, **kwargs)

    class Meta:
        ordering = ("-id", )


class NonrelReservation(models.Model):
    id = djongo_models.ObjectIdField()
    customer_id = djongo_models.IntegerField()
    start_latitude = djongo_models.DecimalField(max_digits=9, decimal_places=6)
    start_longitude = djongo_models.DecimalField(max_digits=9, decimal_places=6)
    srid = djongo_models.CharField(max_length=10)
    net_price = djongo_models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ("-id", )


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    wgs84_polygon = models.TextField()
    the_geom = models.PolygonField()

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.the_geom = GEOSGeometry(self.wgs84_polygon) if self.wgs84_polygon else None

        super(Location, self).save(*args, **kwargs)

    class Meta:
        ordering = ("-id", )


class NonrelLocation(models.Model):
    id = djongo_models.IntegerField(primary_key=True)
    wgs84_polygon = djongo_models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ("-id", )

