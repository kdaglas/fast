from app.database.dbmanager import DatabaseConnection
import psycopg2
from flask import jsonify
from app import app
from flask_jwt_extended import create_access_token
import datetime


dbcon = DatabaseConnection()

'''Object classes for the customer model'''
class Customer():

    def __init__(self, username, contact, password):
        '''Initialising all the parameters'''
        self.username = username
        self.contact = contact
        self.password = password

    
    def register_customer(self):
        '''method that registers or adds a customer to the database'''
        try:
            dbcon.cursor.execute("""INSERT INTO customers(username, contact, password) VALUES (%s, %s, %s)""",
                        (self.username, self.contact, self.password))
            response = jsonify({"message": "{}, your registeration is successful".format(self.username)})
            response.status_code = 201
            return response
        except:
            return jsonify({"message": "Unable to sign you up"})


    def check_for_same_contact(self):
        '''method that if a customer already exists in the database'''
        dbcon.cursor.execute("""SELECT contact FROM customers WHERE contact = %s""",(self.contact,))
        rows = dbcon.cursor.fetchone()
        return rows


    def check_for_same_credentials(self):
        '''method that if a customer exists in the database'''
        dbcon.cursor.execute("""SELECT username, password FROM customers WHERE username = %s and password = %s""",(self.username, self.password,))
        rows = dbcon.cursor.fetchone()
        return rows

    
    def login(self, username, password):
        """loging in a user"""
        try:
            dbcon.cursor.execute("""SELECT * FROM  customers where username = %s AND password = %s""", (username, password))
            count = dbcon.cursor.rowcount
            result = dbcon.cursor.fetchone()
            if count > 0:
                expires = datetime.timedelta(days=1)
                loggedin_customer = dict(customerId=result[0], username=result[1], password=result[2])
                access_token = create_access_token(identity=loggedin_customer, expires_delta=expires)
                return jsonify({"message": "{}, you have been logged in".format(self.username),
                                "space": "-------------------------------------------------------------------------------------------------------------------------",
                                "token": access_token}), 200
            else:
                return jsonify({"message": "Invalid username or password"}), 401
        except:
            return jsonify({"message": "Unable to log you in"})
