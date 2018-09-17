import unittest
from application.routes import webapp
from run import webapp
from modules.models import Customer, Order
import json


class Test_Orders(unittest.TestCase):
    
    def setUp(self):
        self.client = webapp.test_client()

    
    def tearDown(self):
        self.client = None


    def test_registration(self):

        #  a test for successful user registration 

        response = self.client.post("/api/v1/register", data=json.dumps(
            dict(username="Dag", contact="256755598090", 
                 password="Dag123")), content_type='application/json') 

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Customer successfully registered")
        self.assertEqual(response.status_code, 201)


    def test_user_login_successful(self):

        # Test for successful login 

        response = self.client.post("/api/v1/login", data = json.dumps(
            dict(username = "Dag", password = "Dag123")), content_type = 'application/json')

        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Successfully logged in")
        self.assertEqual(response.status_code, 201)


    def test_place_order(self):

        # a test for successfully placing an order 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(orderId = "4536784291", thetype = "Breakfast", food = "Milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Order successfully placed")
        self.assertEqual(response.status_code, 201)
