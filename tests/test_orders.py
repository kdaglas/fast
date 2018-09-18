import unittest
from application.routes import webapp
from run import webapp
from modules.order_model import Order
import json


class Test_Orders(unittest.TestCase):
    
    def setUp(self):
        self.client = webapp.test_client()

    
    def tearDown(self):
        self.client = None


    def test_place_order(self):

        # a test for successfully placing an order 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "5674684890", orderId = "4536784291", thetype = "Breakfast", food = "Milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Your order has been successfully placed")
        self.assertEqual(response.status_code, 200)
