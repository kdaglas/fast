import unittest
from run import app
from flask import jsonify, json
from app import views

class Test_Orders(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    ''' Test for placing an order '''
    def test_add_order(self):

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
        self.assertEquals(reply["message"], "Your order has been placed")
        self.assertEquals(response.status_code, 201)

    ''' a test for successfully placing an order '''
    def test_place_order_with_invalid_keys(self):

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

    ''' Test for empty customerId validation '''
    def test_with_empty_customerId(self):

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
        self.assertEquals(reply["message"], "CustomerId is missing")
        self.assertEquals(response.status_code, 400)
      
    ''' Test for empty food validation '''
    def test_with_empty_food(self):

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
        self.assertEquals(reply['message'], 'Food is missing')
        self.assertEquals(response.status_code, 400)

    ''' Test for empty quantity validation '''
    def test_with_empty_quantity(self):

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
        self.assertEquals(reply['message'], 'Quantity is missing')
        self.assertEquals(response.status_code, 400)

    ''' Test for empty price validation '''
    def test_with_empty_price(self):

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
        self.assertEquals(reply['message'], 'Price is missing')
        self.assertEquals(response.status_code, 400)

    ''' Test for empty type validation '''
    def test_with_empty_type(self):

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
        self.assertEquals(reply['message'], 'The type is missing')
        self.assertEquals(response.status_code, 400)


    # def test_with_same_data(self):
    #     """ Test for empty content validation """
    #     response = self.app.post("/api/v1/orders", content_type='application/json',
    #                             data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="2000", status="not completed"),)
    #                             )
    #     response = self.app.post("/api/v1/orders", content_type='application/json',
    #                             data=json.dumps(dict(orderId="1", customerId="1", today="17.07.2018", thetype="breakfast", food="milk", quantity="3", price="2000", status="not completed"),)
    #                             )              
    #     reply = json.loads(response.data)
    #     self.assertEquals(reply['message'], 'Make another order')
    #     self.assertEquals(response.status_code, 403)
