from app.database.dbmanager import DatabaseConnection
import psycopg2
import psycopg2.extras as dictionary
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
            return  "{}, your registeration is successful".format(self.username)
        except:
            return "Unable to sign you up"


    def add_admin(self):
        '''method that adds a admin to the database'''
        try:
            dbcon.cursor.execute("""INSERT INTO admin(username, password) VALUES (%s, %s)""",
                        (self.username, self.password))
            return "Admin has been created"
        except:
            return "Unable to sign you up"


    def check_for_same_contact(self):
        '''method that if a customer already exists in the database'''
        dbcon.cursor.execute("""SELECT * FROM customers WHERE contact = %s""",(self.contact,))
        customer = dbcon.cursor.fetchone()
        return customer


    def check_for_same_credentials(self):
        '''method that if a customer exists in the database'''
        dbcon.cursor.execute("""SELECT username, password FROM customers WHERE username = %s and password = %s""",(self.username, self.password,))
        rows = dbcon.cursor.fetchone()
        return rows


    def check_for_admin_credentials(self):
        '''method that if a admin exists in the database'''
        dbcon.cursor.execute("""SELECT username, password FROM admin WHERE username = %s and password = %s""",(self.username, self.password,))
        admin = dbcon.cursor.fetchone()
        return admin


    def get_customer_by_username(self):
        try:
            dbcon.cursor.execute("""SELECT * FROM customers WHERE username = %s""",(self.username,))
            customer = dbcon.cursor.fetchone()
            return customer
        except:
            return "Unable to get customer"


    def get_admin_by_username(self):
        try:
            dbcon.cursor.execute("""SELECT * FROM admin WHERE username = %s""",(self.username,))
            admin = dbcon.cursor.fetchone()
            return admin
        except:
            return "Unable to get admin"


    @staticmethod
    def get_admin_credentials_by_username(username):
        try:
            dbcon.cursor.execute("""SELECT * FROM admin WHERE username = %s""",(username,))
            admin = dbcon.cursor.fetchone()
            return admin
        except:
            return "Unable to get admin"
