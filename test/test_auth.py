import unittest
from run import app
from flask import jsonify, json
from app.modules.customer_model import Customer

class Test_auth(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    # Testing for user registration
    def test_registration(self):

        customer = {
            'username' : "Douglas",
            'emailaddress' : "daglach7@gmail.com",
            'contact' : "+256-755-598090",
            'password' : "Dag1234"
        }
        
        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json')                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Customer has been registered")
        self.assertEqual(response.status_code, 201)

    # Testing for user registration
    def test_registration_with_wrong_keys(self):

        customer = {
            'username' : "Douglas",
            'email' : "daglach7@gmail.com",
            'contact' : "+256-755-598090",
            'password' : "Dag1234"
        }
        
        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json')                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The key or value fields are invalid or missing")
        self.assertEqual(response.status_code, 403)

    # Test for empty username validation
    def test_registration_with_empty_username(self):
        
        customer = {
            'username' : "",
            'emailaddress' : "daglach7@gmail.com",
            'contact' : "+256-755-598090",
            'password' : "Dag1234"
        }
        
        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json')                  
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Username is missing")
        self.assertEqual(response.status_code, 400)
      
    # Testing for empty emailaddress validation
    def test_registration_with_empty_emailaddress(self):

        customer = {
            'username' : "Douglas",
            'emailaddress' : "",
            'contact' : "+256-755-598090",
            'password' : "Dag1234"
        }
        
        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json')
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Email address is missing")
        self.assertEquals(response.status_code, 400)
    
    # Test for empty password validation """
    def test_registration_with_empty_password(self):

        customer = {
            'username' : "Douglas",
            'emailaddress' : "daglach7@gmail.com",
            'contact' : "+256-755-598090",
            'password' : ""
        }
        
        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json') 
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Password is missing")
        self.assertEquals(response.status_code, 400)

    # Test for empty password validation
    def test_registration_with_empty_contact(self):

        customer = {
            'username' : "Douglas",
            'emailaddress' : "daglach7@gmail.com",
            'contact' : "",
            'password' : "Dag1234"
        }
        
        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json')
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Contact is missing")
        self.assertEquals(response.status_code, 400)

    # Test for wrong username validation 
    def test_input_with_wrong_username(self):

        customer = {
            'username' : "Dag4",
            'emailaddress' : "daglach7@gmail.com",
            'contact' : "+256-755-598090",
            'password' : "Dag1234"
        }

        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json')                     
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Username should be in characters")
        self.assertEqual(response.status_code, 400)

    # Test for spaces in username validation
    def test_input_with_spaces_in_username(self):

        customer = {
            'username' : " Douglas",
            'emailaddress' : "daglach7@gmail.com",
            'contact' : "+256-755-598090",
            'password' : "Dag1234"
        }

        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json')                              
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Username should have no spaces")
        self.assertEqual(response.status_code, 400)

    # Test for wrong emailaddress validation
    def test_input_with_wrong_emailaddress(self):

        customer = {
            'username' : "Douglas",
            'emailaddress' : "daglach7l.com",
            'contact' : "+256-755-598090",
            'password' : "Dag1234"
        }

        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json')                                  
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Email address should be like this format 'daglach7@gmail.com'")
        self.assertEqual(response.status_code, 400)

    # Test for wrong contact validation
    def test_input_with_wrong_contact(self):

        customer = {
            'username' : "Douglas",
            'emailaddress' : "daglach7@gmail.com",
            'contact' : "0755598090",
            'password' : "Dag1234"
        }

        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json')                              
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Contact should be like this format '+256-755-598090'")
        self.assertEqual(response.status_code, 400)

    # Test for empty password validation
    def test_input_with_wrong_password(self):

        customer = {
            'username' : "Douglas",
            'emailaddress' : "daglach7@gmail.com",
            'contact' : "+256-755-598090",
            'password' : "fgt5"
        }

        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json')                                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Password must have 7 characters with atleast a lowercase, uppercase letter and a number")
        self.assertEqual(response.status_code, 400)

    # Test for successful login
    def test_user_login_successful(self):

        customer = {
            'username' : "Douglas",
            'password' : "Dag1234"
        }
        
        response = self.client.post("/api/v1/login", data = json.dumps(customer), 
                                    content_type = 'application/json') 
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Customer has been logged in")
        self.assertEquals(response.status_code, 200)

    # Testing for user login
    def test_login_with_wrong_keys(self):

        customer = {
            'username' : "Douglas",
            'passw' : "Dag1234"
        }
        
        response = self.client.post("/api/v1/login", data = json.dumps(customer), 
                                    content_type = 'application/json')                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The key or value fields are invalid or missing")
        self.assertEqual(response.status_code, 403)

    # Test for login with wrong or no username
    def test_user_login_with_no_username(self):
         
        customer = {
            'username' : "",
            'password' : "Dag1234"
        }
        
        response = self.client.post("/api/v1/login", data = json.dumps(customer), 
                                    content_type = 'application/json')            
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Username is missing")
        self.assertEquals(response.status_code, 400)

    # Test for login with wrong or no password
    def test_user_login_with_no_password(self):
        
        customer = {
            'username' : "Douglas",
            'password' : ""
        }

        response = self.client.post("/api/v1/login", data = json.dumps(customer), 
                                    content_type = 'application/json')            
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Password is missing")
        self.assertEquals(response.status_code, 400)
