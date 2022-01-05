from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from core import views

urlpatterns = [
    path("locations", views.LocationList.as_view(), name="location_list"),
    path("locations-nonrel", views.NonrelLocationList.as_view(), name="nonrel_location_list"),
    path("reservations", views.ReservationList.as_view(), name="location_list"),
    path("reservations-nonrel", views.NonrelReservationList.as_view(), name="nonrel_location_list"),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'csv'])

