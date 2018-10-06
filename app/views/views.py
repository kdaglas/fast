''' These are the imports for the required packages '''
from app.database.dbmanager import DatabaseConnection
import psycopg2.extras
from app import app
from app.validate import Validator
import json
from flask import request, jsonify
from app.modules.customer_model import Customer

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
    except:
        response = jsonify({"Error": "Some fields are missing, please check"})
        response.status_code = 403
        return response


@app.route("/api/v2/auth/login", methods=['POST'])
def login():
    
    ''' This fuction through the POST method, logins in the customer and returns that him or her and if
        the customer doesnot exist, then it returns 404 '''
    try:
        reg_info = request.get_json()
        username = reg_info.get('username')
        password = reg_info.get('password')

        valid = Validator.validate_login_inputs(reg_info['username'], reg_info['password'])
        '''Validating customer login'''
        if valid == True:
            customer_data = Customer(reg_info['username'], None, reg_info['password'])
            same_data = customer_data.check_for_same_credentials()
            if same_data:
                model = Customer(username, None, password)
                logged_in = model.login(reg_info["username"], reg_info["password"])
                return logged_in 
            return jsonify({"message": "These credentials are invalid or missing"}), 400
        return valid
    except:
        response = jsonify({"Error": "Some fields are missing, please check"})
        response.status_code = 403
        return response
