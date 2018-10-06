from tests.test_base import Testing
from app import app


class CustomerTests(Testing):

    def test_wrong_url(self):
        '''test for checking for wrong url'''


    def test_register_customer(self):
        '''test for registering a customer'''
        tester = self.app.test_client(self)
        response = tester.post('/api/v2/auth/user/signup', data = Testing.register_customer,
                               content_type="application/json")
        # self.assertEqual(response.status_code, 200)
        # self.assertIn(b"registeration successfuly", response.data)
        # self.assertIn(reply["message"], "registeration successfuly")
        self.assertIn("Douglas", str(response.json['message']))

    def test_duplicate_username(self):
        """test method to check for same data"""
        tester = self.app.test_client(self)
        # response = tester.post('/api/v2/auth/user/signup', data = Testing.same_customer,

    def setUp(self):
        self.app = app.test_client()

    def test_register_customer(self):
        '''test registering a customer'''
        response = self.app.post('/api/v2/auth/user/signup', data = Testing.register_customer,
                               content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"registration successful", response.data)


    def test_duplicate_username(self):
        """test method to check for same data"""
        response = self.app.post('/api/v2/auth/user/signup', data = Testing.same_customer,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"username or email is already used", response.data)
                              
    def test_username(self):
        """test for checking correct username"""
        response = self.app.post('/api/v2/auth/user/signup', data=Testing.invaliduser,
                               content_type="application/json")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Username should be in characters", response.data)

    def testing_for_wrong_url(self):
        """test for wrong url"""
        response = self.app.get('/api/v2/me',
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)


    def test_empty_username(self):
        """test for checking empty username"""
        response = self.app.post('/api/v2/auth/user/signup', data=Testing.empty_username,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Username should be in characters", response.data)