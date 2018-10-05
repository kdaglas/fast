from app.database.dbmanager import DatabaseConnection
import psycopg2
from flask import jsonify
from app import app
from flask_jwt_extended import create_access_token
import datetime

'''Object classes for the customer model'''

class Customer(DatabaseConnection):

    def __init__(self, username, contact, password):
        '''Initialising all the parameters'''
        DatabaseConnection.__init__(self)
        self.username = username
        self.contact = contact
        self.password = password

    
    def register_customer(self, username, contact, password):
        '''method that registers or adds a customer to the database'''
        cur = self.con.cursor()
        cur.execute("""INSERT INTO customers(username, contact, password) VALUES (%s, %s, %s)""",
                    (self.username, self.contact, self.password))
        self.con.commit()
        response = jsonify({"message": "registration successful"})
        response.status_code = 200
        return response


    def check_for_same(self):
        '''method that if a customer already exists in the database'''
        cur = self.con.cursor()
        cur.execute("""SELECT username, contact FROM customers WHERE username = %s and contact = %s""",(self.username, self.contact,))
        rows = cur.fetchone()
        return rows


    def check_for_same_stuff(self):
        '''method that if a customer exists in the database'''
        cur = self.con.cursor()
        cur.execute("""SELECT username, password FROM customers WHERE username = %s and password = %s""",(self.username, self.password,))
        rows = cur.fetchone()
        return rows

    
    def login(self, username, password):
        """loging in a user"""
        try:
            response = ""
            cur = self.con.cursor()
            cur.execute("""SELECT * FROM  customers where username = %s AND
                        password = %s""", (username, password))
            self.con.commit()
            count = cur.rowcount
            result = cur.fetchone()
            if count > 0:
                expires = datetime.timedelta(days=1)
                loggedin_customer = dict(customerId=result[0], username=result[1], password=result[2])
                access_token = create_access_token(identity=loggedin_customer, expires_delta=expires)
                response = jsonify({"message": "You have been logged in",
                                    "token": access_token}), 200 
            else:
                response = jsonify({"message": "Invalid username or password"}), 403
            return response
        except:
            return jsonify({"message": "Unable to log you in"})

