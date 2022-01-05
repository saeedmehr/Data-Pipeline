from django.contrib import admin
from core.models import Reservation, Location, NonrelReservation, NonrelLocation

admin.site.register(Reservation)
admin.site.register(Location)
admin.site.register(NonrelReservation)
admin.site.register(NonrelLocation)
