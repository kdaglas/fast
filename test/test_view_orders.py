import unittest
from app import views
from run import app
import json

class Test_Get_Orders(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_all_orders(self):

        # a test for getting all orders

        response = self.client.get("/api/v1/orders", content_type = 'application/json')
                                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "All orders have been viewed")
        self.assertEqual(response.status_code, 302)


    # def test_get_all_orders_emty_list(self):
    #     """ a test for getting all entries """
    #     response = self.app.post("/api/v1/orders", content_type='application/json',
    #                             data=json.dumps(dict(orderId="", customerId="", today="", thetype="", food="", quantity="", price="", status="not completed"),)
    #                             )
                  
    #     reply = json.loads(response.data.decode())
    #     response2 = self.app.get("/api/v1/orders",
    #                             content_type='application/json', data=reply)
    #     reply2 = json.loads(response2.data.decode())
    #     self.assertEquals(reply2["message"],"No order added")


    def test_get_single_order(self):

        # Test to fetch single order

        response = self.client.get("/api/v1/orders/4536784291", content_type = 'application/json')
                                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "One order has been viewed")
        self.assertEqual(response.status_code, 302)


    # def test_get_single_order_with_wrong_id(self):

    #     # Test to fetch single order

    #     response = self.client.get("/api/v1/orders/0",
    #                             content_type='application/json')
    #     reply = json.loads(response.data.decode())
    #     self.assertEquals(reply["message"], "order doesnot exist")
    #     self.assertEqual(response.status_code, 404)

