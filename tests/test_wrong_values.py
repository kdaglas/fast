import unittest
from apis.application.routes import webapp
# from apis.application import routes
# from run import webapp
from apis.modules.customer_model import Customer
from apis.modules.order_model import Order
import json


class Test_For_Wrong_Values(unittest.TestCase):
    
    def setUp(self):
        self.client = webapp.test_client()

    
    def tearDown(self):
        self.client = None


    # These are the tests for validating a customer's registration

    def test_input_with_wrong_username(self):

        # Test for wrong username validation 

        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "2dag", contact = "+256-755-598090", 
                 password = "Dag1234")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Your username should be in characters")
        self.assertEqual(response.status_code, 400)


    def test_input_with_spaces_in_username(self):

        # Test for spaces in username validation 

        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = " dag", contact = "+256-755-598090", 
                 password = "Dag1234")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Your username should have no spaces")
        self.assertEqual(response.status_code, 400)


    def test_input_with_wrong_contact(self):

        # Test for wrong contact validation 

        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Dag", contact = "0755598090", 
                 password = "Dag1234")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Your contact should be in this format +256-755-598090")
        self.assertEqual(response.status_code, 400)


    def test_input_with_wrong_password(self):

        # Test for empty password validation 

        response = self.client.post("/api/v1/register", data = json.dumps(
            dict(username = "Dag", contact = "+256-755-598090", 
                 password = "fgt5")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Your password must have 7 characters with atleast a lowercase and uppercase letter and 1 number")
        self.assertEqual(response.status_code, 400)




    # These are the tests for validating order inputs

    def test_input_with_wrong_customerId(self):

        # Test for wrong customerId type validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "me", orderId = "0987654321", thetype = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The customer's id should be a number")
        self.assertEqual(response.status_code, 400)
    
    
    def test_input_with_wrong_type(self):

        # Test for wrong type validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890", orderId = "0987654321", thetype = "123", food = "milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The type of food should be in characters")
        self.assertEqual(response.status_code, 400)


    def test_input_with_space_in_type(self):

        # Test for spaces in type validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890", orderId = "0987654321", thetype = " breakfast", food = "milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The type of food should have no spaces")
        self.assertEqual(response.status_code, 400)


    def test_input_with_wrong_food(self):

        # Test for wrong food validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890",orderId = "0987654321", thetype = "breakfast", food = "123", 
                 price = "2000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                            
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The food should be in characters")
        self.assertEqual(response.status_code, 400)


    def test_input_with_wrong_price(self):

        # Test for wrong price validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890", orderId = "0987654321", thetype = "breakfast", food = "milk and bread", 
                 price = "me", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The price should be in numbers")
        self.assertEqual(response.status_code, 400)


    def test_input_with_spaces_in_price(self):

        # Test for space in price validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890", orderId = "0987654321", thetype = "breakfast", food = "milk and bread", 
                 price = "20 000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The price should have no spaces")
        self.assertEqual(response.status_code, 400)


    def test_input_with_wrong_quantity(self):

        # Test for wrong quantity validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890", orderId = "0987654321", thetype = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "nuts", today = "2018-09-16")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The quantity should be a number")
        self.assertEqual(response.status_code, 400)


    def test_input_with_space_in_quantity(self):

        # Test for space in quantity validation 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890", orderId = "0987654321", thetype = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "4 ", today = "2018-09-16")), content_type = 'application/json')
                                           
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The quantity should have no spaces")
        self.assertEqual(response.status_code, 400)
