import time

from django.test import TestCase

from rcs_back.containers_app.models import *
from rcs_back.takeouts_app.models import *


class ContainerModelTests(TestCase):

    def setUp(self):
        self.building_with_bparts = Building.objects.create(
            address="ул. Тестовая 25",
        )

        self.building_part = BuildingPart.objects.create(
            building=self.building_with_bparts,
            num=1
        )

        self.building = Building.objects.create(
            address="ул. Тестовая 30"
        )  # Здание без корпусов

        self.condition_for_building_with_bparts = TakeoutCondition.objects.get(
            building=self.building_with_bparts
        )
        self.condition_for_building_with_bparts.ignore_reports = 1
        self.condition_for_building_with_bparts.public_days = 1
        self.condition_for_building_with_bparts.office_days = 2
        self.condition_for_building_with_bparts.save()

        self.condition_for_bpart = TakeoutCondition.objects.get(
            building_part=self.building_part
        )
        self.condition_for_bpart.ignore_reports = 2
        self.condition_for_bpart.public_days = 3
        self.condition_for_bpart.office_days = 4
        self.condition_for_bpart.save()

        self.condition_for_building = TakeoutCondition.objects.get(
            building=self.building
        )
        self.condition_for_building.ignore_reports = 3
        self.condition_for_building.public_days = 5
        self.condition_for_building.office_days = 6
        self.condition_for_building.save()

        self.building.refresh_from_db()
        self.building_part.refresh_from_db()

        self.public_container_in_bpart = Container.objects.create(
            kind=Container.PUBLIC_ECOBOX,
            building=self.building_with_bparts,
            building_part=self.building_part,
            floor=1,
            room="1234",
            status=Container.ACTIVE
        )

        self.office_container_in_bpart = Container.objects.create(
            kind=Container.ECOBOX,
            building=self.building_with_bparts,
            building_part=self.building_part,
            floor=1,
            room="1234",
            status=Container.ACTIVE
        )

        self.public_container_in_building = Container.objects.create(
            kind=Container.PUBLIC_ECOBOX,
            building=self.building,
            floor=1,
            room="1234",
            status=Container.ACTIVE
        )

        self.office_container_in_building = Container.objects.create(
            kind=Container.ECOBOX,
            building=self.building,
            floor=1,
            room="1234",
            status=Container.ACTIVE
        )

    def test_is_active(self):

        active_containers = Container.objects.filter(
            status=Container.ACTIVE
        )
        for container in active_containers:
            self.assertTrue(container.is_active())
        all_containers = Container.objects.all()
        inactive_containers = all_containers.difference(active_containers)
        for container in inactive_containers:
            self.assertFalse(container.is_active())

    def test_is_public(self):

        self.assertTrue(self.public_container_in_bpart.is_public())
        self.assertTrue(self.public_container_in_building.is_public())
        self.assertFalse(self.office_container_in_building.is_public())
        self.assertFalse(self.office_container_in_bpart.is_public())

    def test_ignore_reports_count(self):

        self.assertEqual(
            self.office_container_in_bpart.ignore_reports_count(), 0)
        self.assertEqual(
            self.office_container_in_building.ignore_reports_count(), 0)
        self.assertEqual(
            self.public_container_in_bpart.ignore_reports_count(), 2)
        self.assertEqual(
            self.public_container_in_building.ignore_reports_count(), 3)

    def test_get_time_condition_days(self):

        self.assertEqual(
            self.office_container_in_bpart.get_time_condition_days(), 4)
        self.assertEqual(
            self.office_container_in_building.get_time_condition_days(), 6)
        self.assertEqual(
            self.public_container_in_bpart.get_time_condition_days(), 3)
        self.assertEqual(
            self.public_container_in_building.get_time_condition_days(), 5)