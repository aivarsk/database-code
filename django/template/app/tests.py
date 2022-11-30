from django.test import TestCase
from app.models import Dummy


class PersonTestCase(TestCase):
    def setUp(self):
        Dummy.objects.create(name="huh")

    def test_dummy(self):
        pass
