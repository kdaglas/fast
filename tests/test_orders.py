import unittest
from application.routes import webapp
from modules.models import Meal, Order
import json


class Test_Orders(unittest.TestCase):
    
    def setUp(self):
        self.client = webapp.test_client()

    
    def tearDown(self):
        self.client = None


    def test_input_with_empty_type(self):

        # Test for empty type validation 

        client = webapp.test_client(self)
        response = client.post("/api/v1/meals", data = json.dumps(
            dict(thetype = "", food = "Milk and bread", 
                 price = "2000")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "The type of food is missing")
        self.assertEquals(response.status_code, 400)


    def test_input_with_empty_food(self):

        # Test for empty food validation 

        client = webapp.test_client(self)
        response = client.post("/api/v1/meals", data = json.dumps(
            dict(thetype = "Breakfast", food = "", 
                 price = "2000")), content_type = 'application/json')
                                            
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "The food is missing")
        self.assertEquals(response.status_code, 400)


    def test_input_with_empty_price(self):

        # Test for empty price validation 

        client = webapp.test_client(self)
        response = client.post("/api/v1/meals", data = json.dumps(
            dict(thetype = "Breakfast", food = "Milk and bread", 
                 price = "")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "The price is missing")
        self.assertEquals(response.status_code, 400)


    def test_add_meal(self):

        # a test for successful adding an entry """

        client = webapp.test_client(self)
        response = client.post("/api/v1/meals", data = json.dumps(
            dict(thetype = "Breakfast", food = "Milk and bread", 
                 price = "2000")), content_type = 'application/json')
                                
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Meal successfully added")
        self.assertEquals(response.status_code, 201)
