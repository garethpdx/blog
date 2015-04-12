#  from django.utils import unittest
from django.test import TestCase
from django.contrib.auth.models import User

from django.core.urlresolvers import resolve

from views import measure
from models import Category


class TestMeasurementUserRouting(TestCase):
    TEST_USERNAME = 'tess'
    TEST_PASSWORD = 'tuser'

    def test_measurement_routing_for_new_user(self):
        found = resolve('/measurement/{0}/'.format(self.TEST_USERNAME))
        self.assertEqual(found.func, measure)

    def setUp(self):
        self.create_user()

    def create_user(self):
        User.objects.create_user(self.TEST_USERNAME,
                                 password=self.TEST_PASSWORD)


class TestMeasurementCategoryCreation(TestCase):

    def test_category_count(self):
        self.assertEqual(len(Category.objects.all()), 1)

    def setUp(self):
        self.create_category()

    def create_category(self):
        c = Category(name='test', hidden=False)
        c.save()
    
