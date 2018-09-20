import unittest
from apis.application.routes import webapp
from run import webapp
from apis.modules.order_model import Order
import json


class Test_Orders(unittest.TestCase):
    
    def setUp(self):
        self.client = webapp.test_client()

    
    def tearDown(self):
        self.client = None


    def test_registration(self):

        #  a test for successful user registration 

        response = self.client.post("/api/v1/register", data=json.dumps(
            dict(username="Dag", contact="+256-755-598090", 
                 password="Dag1234")), content_type='application/json') 

        result = json.loads(response.data)
        self.assertEqual(result["message"], "Customer successfully registered")
        self.assertEqual(response.status_code, 200)


    # def test_place_same_order(self):

    #     # a test for placing the same order 

    #     response = self.client.post("/api/v1/orders", data = json.dumps(
    #         dict(customerId = "1234567890", orderId = "0987654321", thetype = "breakfast", food = "milk and bread", 
    #              price = "2000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')

    #     response = self.client.post("/api/v1/orders", data = json.dumps(
    #         dict(customerId = "1234567890", orderId = "0987654321", thetype = "breakfast", food = "milk and bread", 
    #              price = "2000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "You have already made this order")
    #     self.assertEqual(response.status_code, 201)


    def test_place_order_with_invalid_keys(self):

        # a test for successfully placing an order 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890", orderId = "0987654321", thety = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16")), content_type = 'application/json')
                                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The key or value fields are invalid or missing")
        self.assertEqual(response.status_code, 403)
    
    
    def test_place_order(self):

        # a test for successfully placing an order 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890", orderId = "0987654321", thetype = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "2", status = "Null", today = "2018-09-16")), content_type = 'application/json')
                                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Your order has been successfully placed")
        self.assertEqual(response.status_code, 201)


    def test_get_all_orders(self):

        # a test for viewing all orders 

        response = self.client.get("/api/v1/orders", content_type = 'application/json')
                                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "All your orders successfully viewed")
        self.assertEqual(response.status_code, 201)


    # def test_get_one_order_with_invalid_id(self):

    #     # a test for viewing one order 

    #     response = self.client.get("/api/v1/orders/me", content_type = 'application/json')
                                
    #     reply = json.loads(response.data)
    #     self.assertEqual(reply["message"], "Your order id should be a number")
    #     self.assertEqual(response.status_code, 400)


    def test_get_one_order(self):

        # a test for viewing one order 

        response = self.client.get("/api/v1/orders/4536784291", content_type = 'application/json')
                                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Your one order successfully viewed")
        self.assertEqual(response.status_code, 201)


    def test_update_an_order(self):

        # a test for updating an order 

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "1234567890", orderId = "0987654321", thetype = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "2", status = "Null", today = "2018-09-16")), content_type = 'application/json')

        response = self.client.put("/api/v1/orders/4536784291", data = json.dumps(
            dict(customerId = "2345678901", orderId = "0987654321", thetype = "lunch", food = "chicken", 
                 price = "4000", quantity = "5", status = "completed", today = "2018-09-16")), content_type = 'application/json')
                                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Your one order successfully updated")
        self.assertEqual(response.status_code, 201)
