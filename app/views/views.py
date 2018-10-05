''' These are the imports for the required packages '''
from app.database.dbmanager import DatabaseConnection
import psycopg2.extras
from app import app
from app.validate import Validator
import json
from flask import request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
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
            customer_data = Customer(reg_info['username'], reg_info['contact'], None)
            same_data = customer_data.check_for_same()
            if same_data:
                return jsonify({"message":"Username and contact already exist, use anothers"}), 400 
            '''Register the customer'''
            obj = Customer(username, contact, password)
            result = obj.register_customer()
            return result
        else:
            return valid
    except:
        response = jsonify({"Error": "Some fields are missing, please check"})
        response.status_code = 403
        return response


@app.route("/api/v2/auth/login", methods=['POST'])
def login():
    
    ''' This fuction through the POST method, logins in the customer and returns that him or her and if
        the customer doesnot exist, then it returns 404 '''
    # try:
    reg_info = request.get_json()
    username = reg_info.get('username')
    password = reg_info.get('password')

    valid = Validator.validate_login_inputs(reg_info['username'], reg_info['password'])
    '''Validating customer login'''
    if valid == True:
        customer_data = Customer(reg_info['username'], None, reg_info['password'])
        same_data = customer_data.check_for_same_stuff()
        if same_data:
            model = Customer(username, None, password)
            logged_in = model.login(reg_info["username"], reg_info["password"])
            return logged_in
        else:
            response = jsonify({"message": "These credentials are invalid or missing"}), 400
            return response
    else:
        return valid

        ''' an imported function that returns the username from the database'''
        
    # except:
    #     response = jsonify({"Error": "Some fields are missing, please check"})
    #     response.status_code = 403
    #     return response








# @app.route("/api/v1/orders/<orderId>", methods=["GET"])
# def get_single_order(orderId):
    
#     ''' This function routes to /api/v1/orders/<ordersId> and uses the GET method to return a particular order made
#         it takes in the order id as its key search value so to return that particular order '''
#     order = Order.get_one_order(orderId)
#     return jsonify({"Your order": order,
#                     'message': 'One order has been viewed'}), 302


# @app.route("/api/v1/orders/<orderId>", methods=["PUT"])
# def edit_order(orderId):
    
#     ''' This function uses the PUT method to update the order status of the order with that given orderId.
#     it takes in an order id and searches for that order with that id and then returns an updated order '''
#     data = request.get_json()
#     status = data.get('status')

#     updated_order = Order.update_order(orderId, status)
#     return jsonify({"Updated order": updated_order,
#                 'message': 'Order status has been updated'}), 201
