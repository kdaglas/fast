''' These are the imports for the required packages '''
import psycopg2.extras
from app import app
from app.validate import Validator
import json
from flask import request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import datetime
from app.database.dbmanager import DatabaseConnection
from app.modules.order_model import Order


@app.route("/api/v2/users/orders", methods=['POST'])
@jwt_required
def place_order():

    ''' This function helps the customer to create or place an order through the POST method
        it takes in input data from the customer preferably the order to be made and
        posts the data returning the order made by the customer '''
    # try:
    data = request.get_json()
    today = str(date.today())
    mealId = data.get('mealId')
    # customerId = data.get('customerId')
    quantity = data.get('quantity')
    status = 'Not complete'

    valid = Validator.validate_registration_inputs(reg_info['username'], reg_info['contact'], reg_info['password'])
    '''Validating and checking for similar data'''
    if valid == True:
        password
    else:
        return valid

    Order.placing_order(customerId, mealId, quantity, status, today)
    placed_order = Order(
        customerId = customerId,
        mealId = mealId,
        quantity = quantity,
        status = status,
        today = today
    )
    return jsonify({'Your order': placed_order.__dict__,
                    'message': 'Order has been placed'}), 200
    # except:
    #     response = jsonify({"message": "The key or value fields are invalid or missing"})
    #     response.status_code = 403
    #     return response


@app.route("/api/v2/users/orders", methods=['GET'])
@jwt_required
def get_all_orders():
    
    ''' This function routes to /api/v1/orders and uses the GET method to return all the orders made '''
    orders = Order.getting_all_orders()
    return jsonify({'All meals': orders,
                    'message': 'All orders have been viewed'}), 201


@app.route("/api/v2/users/orders/<orderId>", methods=['GET'])
@jwt_required
def get_one_order(orderId):
    
    ''' This function routes to /api/v2/orders/<orderId> and uses the GET method to return a single order '''
    order = Order.get_one_order(orderId)
    return jsonify({'All meals': order,
                    'message': 'All meals have been viewed'}), 201