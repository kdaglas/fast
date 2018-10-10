''' These are the imports for the required packages '''
from app.database.dbmanager import DatabaseConnection
import psycopg2
from app import app
from app.validate import Validator
import json
import datetime
from flask_jwt_extended import create_access_token
from flask import request, jsonify
from app.modules.customer_model import Customer


@app.route("/api/v2/auth/adminsignup", methods=['POST'])
def adminsignup():

    ''' This function registers an admin through POST method by taking in
        the input from the user and storing it in the database '''
    try:
        reg_info = request.get_json()
        username = reg_info.get("username")
        password = reg_info.get("password")

        valid = Validator.validate_admin_inputs(reg_info['username'], reg_info['password'])
        '''Validating and checking for similar data'''
        if valid == True:
            admin_info = Customer(reg_info['username'], None, None)
            same_data = admin_info.get_admin_by_username()
            if same_data:
                return jsonify({"message":"Admin already exists"}), 400
            '''Add an administrator'''
            obj = Customer(username, None, password)
            result = obj.add_admin()
            return result
        return valid
    except:
        response = jsonify({"Error": "Some fields are missing, please check"})
        response.status_code = 400
        return response


@app.route("/api/v2/auth/signup", methods=['POST'])
def register():

    ''' This function registers a customer through POST method by taking in
        the input from the user and storing it in the database '''
    try:
        reg_info = request.get_json()
        username = reg_info.get("username")
        contact = reg_info.get("contact")
        password = reg_info.get("password")

        valid = Validator.validate_registration_inputs(reg_info['username'], reg_info['contact'], reg_info['password'])
        '''Validating and checking for similar data'''
        if valid == True:
            customer_data = Customer(None, reg_info['contact'], None)
            same_data = customer_data.check_for_same_contact()
            if same_data:
                return jsonify({"message":"Contact already exists, use another"}), 400
            '''Register the customer'''
            obj = Customer(username, contact, password)
            result = obj.register_customer()
            return result
        return valid
    except Exception as excp:
        print(excp)
        response = jsonify({"Error": "Some fields are missing, please check"})
        response.status_code = 400
        return response


@app.route("/api/v2/auth/adminlogin", methods=['POST'])
def adminlogin():
    
    ''' This fuction through the POST method, logins in the admin and returns that him or her and if
        the customer doesnot exist, then it returns 404 '''
    try:
        reg_info = request.get_json()
        username = reg_info.get('username')
        password = reg_info.get('password')

        admin_data = Customer(reg_info['username'], None, reg_info['password'])
        same_data = admin_data.check_for_admin_credentials()
        if same_data:
            admin = Customer(username, None, password)
            admin_logged_in = admin.get_admin_by_username()
            '''Creating an access token'''
            expires = datetime.timedelta(days=1)
            access_token = create_access_token(identity=admin_logged_in['adminid'], expires_delta=expires)
            return jsonify({"message": "Admin is logged in",
                            "space": "------------------------------This is your token------------------------------------------------------------",
                            "token": access_token}), 200
        return jsonify({"message": "Invalid username or password"}), 401
    except:
        response = jsonify({"message": "Some fields are missing, please check"})
        response.status_code = 400
        return response


@app.route("/api/v2/auth/login", methods=['POST'])
def login():
    
    ''' This fuction through the POST method, logins in the customer and returns that him or her and if
        the customer doesnot exist, then it returns 404 '''
    try:
        reg_info = request.get_json()
        username = reg_info.get('username')
        password = reg_info.get('password')

        customer_data = Customer(reg_info['username'], None, reg_info['password'])
        same_data = customer_data.check_for_same_credentials()
        if same_data:
            model = Customer(username, None, password)
            logged_in = model.get_customer_by_username()
            '''Creating an access token'''
            expires = datetime.timedelta(days=1)
            access_token = create_access_token(identity=logged_in['customerid'], expires_delta=expires)
            return jsonify({"message": "You have been logged in",
                            "space": "-------------------------------------------------------------------------------------------------------------------------",
                            "token": access_token}), 200
        return jsonify({"message": "Invalid username or password"}), 401
    except:
        response = jsonify({"Error": "Some fields are missing, please check"})
        response.status_code = 403
        return response
