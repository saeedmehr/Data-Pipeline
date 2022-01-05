import time
import csv

from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand

from core.tasks import add_location


class Command(BaseCommand):
    """Django command to load locations from CSV file."""

    def add_arguments(self, parser):
        parser.add_argument('csv_files', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.write('Loading locations...')
        for file_path in options['csv_files']:
            self.stdout.write(f'Loading {file_path}')
            with open(file_path) as _file:
                csv_reader = csv.reader(_file)
                for seq, location_id, location_polygon in csv_reader:
                    if not location_id.isdigit():
                        continue
                    add_location.delay(location_id=location_id, location_polygon=location_polygon)

            self.stdout.write(self.style.SUCCESS('Loading finished!'))
