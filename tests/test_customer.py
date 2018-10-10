from tests.test_base import Testing
from app import app
from app.database.dbmanager import DatabaseConnection
import json


dbcon = DatabaseConnection()

class CustomerTests(Testing):

    def setUp(self):
        self.app = app.test_client()
        dbcon.create_tables()


    def test_register_customer_with_invalid_fields(self):
        '''test registering a customer with invalid fields'''
        response = self.app.post('/api/v2/auth/signup', data = Testing.wrong_fields,
                                content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Some fields are missing, please check", response.data)


    def test_register_customer_with_same_contact(self):
        '''test registering a customer with same contact'''
        response = self.app.post('/api/v2/auth/signup', data = Testing.same_contact,
                                content_type="application/json")
        self.assertEqual(response.status_code, 400)


    def test_register_customer(self):
        '''test registering a customer'''
        response = self.app.post('/api/v2/auth/signup', data = Testing.register_customer,
                               content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Douglas, your registeration is successful", response.data)


    def test_register_customer_with_empty_username(self):
        '''test registering a customer'''
        response = self.app.post('/api/v2/auth/signup', data = Testing.empty_username,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Username is missing", response.data)


    def test_register_customer_with_empty_contact(self):
        '''test registering a customer'''
        response = self.app.post('/api/v2/auth/signup', data = Testing.empty_contact,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Contact is missing", response.data)


    def test_register_customer_with_empty_password(self):
        '''test registering a customer'''
        response = self.app.post('/api/v2/auth/signup', data = Testing.empty_password,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Password is missing", response.data)


    def test_login_customer_with_empty_password(self):
        '''test registering a customer'''
        response = self.app.post('/api/v2/auth/signup', data = Testing.empty_password,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Password is missing", response.data)


    # def test_duplicate_username(self):
    #     """test method to check for same data"""
    #     response = self.app.post('/api/v2/auth/user/signup', data = Testing.same_customer,
    #                            content_type="application/json")
    #     self.assertEqual(response.status_code, 400)
    #     self.assertIn(b"username or email is already used", response.data)
                              
    # def test_username(self):
    #     """test for checking correct username"""
    #     response = self.app.post('/api/v2/auth/user/signup', data=Testing.invaliduser,
    #                            content_type="application/json")
    #     self.assertEqual(response.status_code, 404)
    #     self.assertIn(b"Username should be in characters", response.data)

    # def testing_for_wrong_url(self):
    #     """test for wrong url"""
    #     response = self.app.get('/api/v2/me',
    #                           content_type="application/json")
    #     self.assertEqual(response.status_code, 404)


    # def test_empty_username(self):
    #     """test for checking empty username"""
    #     response = self.app.post('/api/v2/auth/user/signup', data=Testing.empty_username,
    #                            content_type="application/json")
    #     self.assertEqual(response.status_code, 400)
    #     self.assertIn(b"Username should be in characters", response.data)