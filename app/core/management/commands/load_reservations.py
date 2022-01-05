import time
import csv

from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand

from core.tasks import add_reservation


class Command(BaseCommand):
    """Django command to load reservations from CSV file."""

    def add_arguments(self, parser):
        parser.add_argument('csv_files', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.write('Loading reservations...')
        for file_path in options['csv_files']:
            self.stdout.write(f'Loading {file_path}')
            with open(file_path) as _file:
                csv_reader = csv.reader(_file)
                for seq, _id, customer_id, start_latitude, start_longitude, srid, net_price in csv_reader:
                    if not _id.isdigit():
                        continue
                    add_reservation.delay(
                        _id=_id,
                        customer_id=customer_id,
                        start_latitude=start_latitude,
                        start_longitude=start_longitude,
                        srid=srid,
                        net_price=net_price,
                    )

            self.stdout.write(self.style.SUCCESS('Loading finished!'))
