import unittest
from run import app
import json

class Test_Edit_Entry(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    
    def test_edit_order(self):
        ''' Test to modify single diary '''
        order = {
            'customerId' : "12345",
            'thetype' : "breakfast",
            'food' : "milk and bread",
            'price' : "2000",
            'quantity' : "2"
        }
        response = self.client.post("/api/v1/orders", data = json.dumps(order), 
                                    content_type = 'application/json')
        order = {
            'customerId' : "12345",
            'thetype' : "breakfast",
            'food' : "milk and bread",
            'price' : "2000",
            'quantity' : "2",
            'status' : "completed"
        }
        response = self.client.put("/api/v1/orders/09876", data = json.dumps(order), 
                                    content_type = 'application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Order status has been updated")
