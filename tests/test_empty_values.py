import unittest
from application.routes import webapp
from modules.models import Meal, Order
import json


class Test_For_Empty_Values(unittest.TestCase):
    
    def setUp(self):
        self.client = webapp.test_client()

    
    def tearDown(self):
        self.client = None


    def test_input_with_empty_type(self):

        # Test for empty type validation 

        response = self.client.post("/api/v1/meals", data = json.dumps(
            dict(thetype = "", food = "Milk and bread", 
                 price = "2000")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "The type of food is missing")
        self.assertEquals(response.status_code, 400)


    def test_input_with_empty_food(self):

        # Test for empty food validation 

        response = self.client.post("/api/v1/meals", data = json.dumps(
            dict(thetype = "Breakfast", food = "", 
                 price = "2000")), content_type = 'application/json')
                                            
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "The food is missing")
        self.assertEquals(response.status_code, 400)


    def test_input_with_empty_price(self):

        # Test for empty price validation 

        response = self.client.post("/api/v1/meals", data = json.dumps(
            dict(thetype = "Breakfast", food = "Milk and bread", 
                 price = "")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "The price is missing")
        self.assertEquals(response.status_code, 400)


    def test_input_with_empty_food_for_the_order(self):

        # Test for empty mealId validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(food = "", quantity = "2")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "The food is missing")
        self.assertEquals(response.status_code, 400)


    def test_input_with_empty_quantity(self):

        # Test for empty quantity validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(mealId = "9870654386", quantity = "")), content_type = 'application/json')
                                            
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "The quantity is missing")
        self.assertEquals(response.status_code, 400)
