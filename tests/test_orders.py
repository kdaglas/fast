import unittest
from application.routes import webapp
from modules.models import Meal, Order
import json


class Test_Orders(unittest.TestCase):
    
    def setUp(self):
        self.client = webapp.test_client()

    
    def tearDown(self):
        self.client = None


    def test_add_meal(self):

        # a test for successfully adding a meal 

        response = self.client.post("/api/v1/meals", data = json.dumps(
            dict(thetype = "Breakfast", food = "Milk and bread", 
                 price = "2000")), content_type = 'application/json')
                                
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Meal successfully added")
        self.assertEquals(response.status_code, 201)


    def test_place_order(self):

        # a test for successfully placing an order 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(thetype = "Breakfast", food = "Milk and bread", 
                 price = "2000", quantity = "2")), content_type = 'application/json')
                                
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Order successfully made")
        self.assertEquals(response.status_code, 201)
