import datetime

from django.core.urlresolvers import resolve, Resolver404
from django.test import TestCase
from django.http import HttpRequest

from openshift.views import go404
from openshift.views import index

from openshift.blogs.models import Post

class SuccessfulRoutingTest(TestCase):
    def setUp(self):
        self.expected_function = None
        self.urls = []

    def test_resolution_of_page(self):
        for url in self.urls:
            found = resolve(url)
            self.assertEqual(found.func, self.expected_function)


class HomepageRoutingTest(SuccessfulRoutingTest):
    def setUp(self):
        self.expected_function = index
        self.urls = ['/']


class NonRouteFailure(TestCase):
    def setUp(self):
        self.expected_function = go404
        self.urls = ['/232352sadasae','/blogg/']

    def test_routes(self):
        for url in self.urls:
            encountered_404 = False
            try:
                resolve(url)
            except Resolver404:
                encountered_404 = True
            self.assertTrue(encountered_404)


class RequestTest(TestCase):
    def setUp(self):
        self.request = HttpRequest()
        self.urls = []

    def test_page_http_status(self):
        for url in self.urls:
            found = resolve(url)
            resp = self.get_response(found.func)
            self.assertEqual(resp.status_code, 200)

    def get_response(self, resolver):
        return resolver(self.request)
    

class HomePageRequestTest(RequestTest):
    def setUp(self):
        self.request = HttpRequest()
        self.urls = ['/']


class BlogPostRequestTest(RequestTest):
    @staticmethod
    def create_example_post():
        post = Post(content='test content',
                         date=datetime.datetime(2014, 10, 07),
                         title='test post title', blob='test_post',
                         hidden=False)
        post.save()
        return post
    
    def setUp(self):
        self.request = HttpRequest()
        self.post = self.create_example_post()
        self.urls = ['/2012/02/{0}/'.format(self.post.blob)]

    def get_response(self, resolver):
        return resolver(self.request, post_name=self.post.blob)
