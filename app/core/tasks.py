from .models import Reservation, Location, NonrelReservation, NonrelLocation
from celery import shared_task


@shared_task
def add_location(location_id, location_polygon):
    params = dict(
        id=location_id,
        defaults={'wgs84_polygon': location_polygon},
    )
    try:
        Location.objects.update_or_create(**params)
    except Exception as e:
        # TODO: Implement a better handler
        pass

    try:
        NonrelLocation.objects.update_or_create(**params)
    except Exception as e:
        # TODO: Implement a better handler
        pass


@shared_task
def add_reservation(_id, customer_id, start_latitude, start_longitude, srid, net_price):
    params = dict(
        id=_id,
        defaults={
            'customer_id': customer_id,
            'start_latitude': start_latitude,
            'start_longitude': start_longitude,
            'srid': srid,
            'net_price': net_price,
        },
    )
    try:
        Reservation.objects.update_or_create(**params)
    except Exception as e:
        # TODO: Implement a better handler
        pass

    try:
        NonrelReservation.objects.update_or_create(**params)
    except Exception as e:
        # TODO: Implement a better handler
        pass
