import unittest
from application.routes import webapp
from modules.models import Meal, Order


class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.client = webapp.test_client()
    
    def tearDown(self):
        self.client = None
