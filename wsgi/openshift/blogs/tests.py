from django.core.urlresolvers import resolve

from django.utils import unittest
#  from django.test import TestCase
from openshift.blogs.views import index


class HomePageTest(unittest.TestCase):
    def test_resolution_of_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, index)



