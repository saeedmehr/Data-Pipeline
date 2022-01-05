from unittest import mock

from django.test import TestCase

from core.tasks import add_location


# Create your tests here.
class TaskTestCase(TestCase):
    @mock.patch('core.tasks.Location')
    def test_add_location(self, location_mock):
        add_location(location_id="FOO", location_polygon="BAR")
        location_mock.objects.update_or_create.assert_called_once_with(
            id="FOO",
            defaults={'wgs84_polygon': "BAR"},
        )
