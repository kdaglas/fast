import unittest
from run import app
from flask import jsonify, json
from app.modules.customer_model import Customer

class Test_auth(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()


    def test_registration(self):
        '''Testing for user registration'''
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


    def test_registration_with_wrong_keys(self):
        '''Testing for user registration with wrong keys'''
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


    def test_registration_with_empty_username(self):
        '''Test for empty username validation'''
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
      

    def test_registration_with_empty_emailaddress(self):
        '''Testing for empty emailaddress validation'''
        customer = {
            'username' : "Douglas",
            'emailaddress' : "",
            'contact' : "+256-755-598090",
            'password' : "Dag1234"
        }
        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Email address is missing")
        self.assertEqual(response.status_code, 400)
    

    def test_registration_with_empty_password(self):
        '''Test for empty password validation'''
        customer = {
            'username' : "Douglas",
            'emailaddress' : "daglach7@gmail.com",
            'contact' : "+256-755-598090",
            'password' : ""
        }
        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json') 
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Password is missing")
        self.assertEqual(response.status_code, 400)
    

    def test_registration_with_empty_contact(self):
        '''Test for empty contact validation'''
        customer = {
            'username' : "Douglas",
            'emailaddress' : "daglach7@gmail.com",
            'contact' : "",
            'password' : "Dag1234"
        }
        response = self.client.post("/api/v1/register", data = json.dumps(customer), 
                                    content_type = 'application/json')
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Contact is missing")
        self.assertEqual(response.status_code, 400)

    
    def test_input_with_wrong_username(self):
        '''Test for wrong username validation'''
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

    
    def test_input_with_spaces_in_username(self):
        '''Test for spaces in username validation'''
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

    
    def test_input_with_wrong_emailaddress(self):
        '''Test for wrong emailaddress validation'''
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

    
    def test_input_with_wrong_contact(self):
        '''Test for wrong contact validation'''
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

    
    def test_input_with_wrong_password(self):
        '''Test for empty password validation'''
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

    
    def test_user_login_successful(self):
        '''Test for successful login'''
        customer = {
            'username' : "Douglas",
            'password' : "Dag1234"
        }
        response = self.client.post("/api/v1/login", data = json.dumps(customer), 
                                    content_type = 'application/json') 
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Customer has been logged in")
        self.assertEqual(response.status_code, 200)

    
    def test_login_with_wrong_keys(self):
        '''Testing for user login with wrong keys'''
        customer = {
            'username' : "Douglas",
            'passw' : "Dag1234"
        }
        response = self.client.post("/api/v1/login", data = json.dumps(customer), 
                                    content_type = 'application/json')                
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "The key or value fields are invalid or missing")
        self.assertEqual(response.status_code, 403)

    
    def test_user_login_with_no_username(self):
        '''Test for login with wrong or no username'''
        customer = {
            'username' : "",
            'password' : "Dag1234"
        }
        response = self.client.post("/api/v1/login", data = json.dumps(customer), 
                                    content_type = 'application/json')            
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Username is missing")
        self.assertEqual(response.status_code, 400)

    
    def test_user_login_with_no_password(self):
        '''Test for login with wrong or no password'''
        customer = {
            'username' : "Douglas",
            'password' : ""
        }
        response = self.client.post("/api/v1/login", data = json.dumps(customer), 
                                    content_type = 'application/json')            
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Password is missing")
        self.assertEqual(response.status_code, 400)
