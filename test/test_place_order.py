import unittest
from run import app
from flask import jsonify, json
from app import views

class Test_Orders(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    
    def test_add_order(self):
        ''' Test for placing an order '''
        order = {
            'customerId' : "12345",
            'thetype' : "breakfast",
            'food' : "milk and bread",
            'price' : "2000",
            'quantity' : "2"
        }
        response = self.client.post("/api/v1/orders", data = json.dumps(order), 
                                    content_type = 'application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Your order has been placed")
        self.assertEqual(response.status_code, 201)

    
    def test_place_order_with_invalid_keys(self):
        ''' a test for successfully placing an order '''
        order = {
            'customerId' : "12345",
            'the' : "breakfast",
            'food' : "milk and bread",
            'price' : "2000",
            'quantity' : "2"
        }
        response = self.client.post("/api/v1/orders", data = json.dumps(order), 
                                    content_type = 'application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The key or value fields are invalid or missing")
        self.assertEqual(response.status_code, 403)

    
    def test_with_empty_customerId(self):
        ''' Test for empty customerId validation '''
        order = {
            'customerId' : "",
            'thetype' : "breakfast",
            'food' : "milk and bread",
            'price' : "2000",
            'quantity' : "2"
        }
        response = self.client.post("/api/v1/orders", data = json.dumps(order), 
                                    content_type = 'application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "CustomerId is missing")
        self.assertEqual(response.status_code, 400)
      
    
    def test_with_empty_food(self):
        ''' Test for empty food validation '''
        order = {
            'customerId' : "12345",
            'thetype' : "breakfast",
            'food' : "",
            'price' : "2000",
            'quantity' : "2"
        }
        response = self.client.post("/api/v1/orders", data = json.dumps(order), 
                                    content_type = 'application/json') 
        reply = json.loads(response.data)
        self.assertEqual(reply['message'], 'Food is missing')
        self.assertEqual(response.status_code, 400)

    
    def test_with_empty_quantity(self):
        ''' Test for empty quantity validation '''
        order = {
            'customerId' : "12345",
            'thetype' : "breakfast",
            'food' : "milk and bread",
            'price' : "2000",
            'quantity' : ""
        }
        response = self.client.post("/api/v1/orders", data = json.dumps(order), 
                                    content_type = 'application/json') 
        reply = json.loads(response.data)
        self.assertEqual(reply['message'], 'Quantity is missing')
        self.assertEqual(response.status_code, 400)

    
    def test_with_empty_price(self):
        ''' Test for empty price validation '''
        order = {
            'customerId' : "12345",
            'thetype' : "breakfast",
            'food' : "milk and bread",
            'price' : "",
            'quantity' : "2"
        }
        response = self.client.post("/api/v1/orders", data = json.dumps(order), 
                                    content_type = 'application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply['message'], 'Price is missing')
        self.assertEqual(response.status_code, 400)

    
    def test_with_empty_type(self):
        ''' Test for empty type validation '''
        order = {
            'customerId' : "12345",
            'thetype' : "",
            'food' : "milk and bread",
            'price' : "2000",
            'quantity' : "2"
        }
        response = self.client.post("/api/v1/orders", data = json.dumps(order), 
                                    content_type = 'application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply['message'], 'The type is missing')
        self.assertEqual(response.status_code, 400)
