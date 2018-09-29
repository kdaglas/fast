import unittest
from app import views
from run import app
import json

class Test_Get_Orders(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    
    def test_get_all_orders(self):
        ''' a test for getting all orders '''
        response = self.client.get("/api/v1/orders", content_type = 'application/json')       
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "All orders have been viewed")
        self.assertEqual(response.status_code, 302)


    def test_get_single_order(self):
        ''' Test to fetch single order '''
        response = self.client.get("/api/v1/orders/09876", content_type = 'application/json')  
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "One order has been viewed")
        self.assertEqual(response.status_code, 302)
