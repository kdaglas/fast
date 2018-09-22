import unittest
# from app import views
from run import app
import json

class Test_Edit_Entry(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_edit_order(self):

        # Test to modify single diary

        response = self.client.post("/api/v1/orders", data = json.dumps(
            dict(customerId = "12345", orderId = "09876", thetype = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16", status="not completed")), content_type = 'application/json')

        response = self.client.put("/api/v1/orders/09876", data = json.dumps(
            dict(customerId = "12345", orderId = "09876", thetype = "breakfast", food = "milk and bread", 
                 price = "2000", quantity = "2", today = "2018-09-16", status="not completed")), content_type = 'application/json')

        data = json.loads(response.data.decode())
        self.assertEquals(data["message"], "Order status has been updated")
