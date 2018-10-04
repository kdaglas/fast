from tests.test_base import Testing


class CustomerTests(Testing):

    def test_register_customer(self):
        '''test registering a customer'''
        tester = self.app.test_client(self)
        response = tester.post('/api/v2/auth/user/signup',
                               data = Testing.register_customer,
                               content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"registeration successfuly", response.data)

    def test_duplicate_username(self):
        """test method to check for same data"""
        tester = self.app.test_client(self)
        response = tester.post('/api/v2/auth/user/signup',
                               data = Testing.same_customer,
                               content_type="application/json")
        self.assertEqual(response.status_code, 409)
        self.assertIn(b"username or email is already used", response.data)
                              

    def test_username(self):
        """test for checking correct username"""
        tester = self.app.test_client(self)
        response = tester.post('/api/v2/auth/user/signup',
                               data=Testing.invaliduser,
                               content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Username should be in characters", response.data)


    def testing_for_wrong_url(self):
        """test for wrong url"""
        tester = self.app.test_client(self)
        response = tester.get('/api/v2/me',
                              content_type="application/json")
        self.assertEqual(response.status_code, 404)
