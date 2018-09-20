import unittest
from apis.application.routes import webapp
from run import webapp
from apis.modules.customer_model import Customer
from apis.modules.order_model import Order
import json


class Test_For_Empty_Values(unittest.TestCase):
    
    def setUp(self):
        self.client = webapp.test_client()

    
    def tearDown(self):
        self.client = None


    # These are the tests for validating a customer's registration

    def test_input_with_empty_username(self):

        # Test for empty username validation 

        
        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "", contact = "+256-755-598090", 
                password = "Dag1234")), content_type = 'application/json')
                                        
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Your username is missing")
        self.assertEqual(response.status_code, 400)
        


    def test_input_with_empty_contact(self):

        # Test for empty contact validation 

        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Dag", contact = "", 
                 password = "Dag1234")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Your contact is missing")
        self.assertEqual(response.status_code, 400)


    def test_input_with_empty_password(self):

        # Test for empty password validation 

        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Dag", contact = "+256-755-598090", 
                 password = "")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Your password is missing")
        self.assertEqual(response.status_code, 400)


    # These are the tests for validating order inputs

    def test_input_with_empty_customerId(self):

        # Test for empty customer validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "", orderId = "0987654321", thetype = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The customer's id is missing")
        self.assertEqual(response.status_code, 400)
    
    
    def test_input_with_empty_type(self):

        # Test for empty type validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890", orderId = "0987654321", thetype = "", food = "milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The type of food is missing")
        self.assertEqual(response.status_code, 400)


    def test_input_with_empty_food(self):

        # Test for empty food validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890",orderId = "0987654321", thetype = "breakfast", food = "", 
                 price = "2000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                            
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The food is missing")
        self.assertEqual(response.status_code, 400)


    def test_input_with_empty_price(self):

        # Test for empty price validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890", orderId = "0987654321", thetype = "breakfast", food = "milk and bread", 
                 price = "", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The price is missing")
        self.assertEqual(response.status_code, 400)


    def test_input_with_empty_quantity(self):

        # Test for empty quantity validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890", orderId = "0987654321", thetype = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "", today = "2018-09-16")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The quantity is missing")
        self.assertEqual(response.status_code, 400)
