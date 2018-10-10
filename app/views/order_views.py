''' These are the imports for the required packages '''
from app.database.dbmanager import DatabaseConnection
import psycopg2.extras
from app import app
from app.validate import Validator
import json
from datetime import date
from flask import request, jsonify
from app.modules.order_model import Order
from flask_jwt_extended import jwt_required, get_jwt_identity


@app.route("/api/v2/users/orders", methods=['POST'])
@jwt_required
def place_order():

    ''' This function helps the customer to create or place an order through the POST method
        it takes in input data from the customer preferably the order to be made and
        posts the data returning the order made by the customer '''
    try:
        customer = get_jwt_identity()
        data = request.get_json()
        mealId = data.get('mealId')
        quantity = data.get('quantity')
        status = 'Not complete'

        ordered_food = Order.check_and_return_mealId(mealId)
        print(ordered_food)
        if ordered_food:
            '''Do some validation from the database'''
            print(customer)
            order = Order(customer, mealId, quantity, status)
            placed_order = order.get_food_by_id(mealId)  
            if placed_order:
                return jsonify({"message":"Order has already been placed, place another"}), 403 
            '''Place an order'''
            result = order.place_order()
            return jsonify({"message": result}), 200
        return jsonify({"message":"Meal id does not exist, choose another"}), 403 

    # valid = Validator.validate_order_inputs(data['food'], data['quantity'])
    # '''Validating and checking for similar data'''
    # if valid == True:
    # order_data = Order(data['food'], None, None, None)
    # same_data = order_data.check_and_return_food()
    # if same_data:
    #     return jsonify({"message":"Order already exists, place another"}), 400 
    
    # obj = Order(customerId, food, quantity, status, today)
    # result = obj.place_order()
    # return result

    # new_order = Order(food, quantity, status, today)
    # placed_order = Order.place_order(new_order)
    # return jsonify({'Placed order': placed_order,
    #                 'message': 'Your order placed'}), 201

    # return valid
    except:
        response = jsonify({"message": "The key or value fields are invalid or missing"})
        response.status_code = 403
        return response


@app.route("/api/v2/orders", methods=['GET'])
# @jwt_required
def get_all_the_orders():
    
    ''' This function routes to /api/v2/users/orders and uses the GET method to return all the orders made '''
    orders = Order.get_all_orders()
    if not orders:
        return jsonify({"message": "No orders made yet"}), 404 
    return jsonify({'All meals': orders,
                    'message': 'All orders have been viewed'}), 201


@app.route("/api/v2/orders/<orderId>", methods=['GET'])
@jwt_required
def get_one_order(orderId):
    
    ''' This function routes to /api/v2/orders/<orderId> and uses the GET method to return a single order '''
    order = Order.get_order_by_id(orderId)
    return jsonify({'All meals': order,
                    'message': 'The order have been viewed'}), 201


@app.route("/api/v1/orders/<orderId>", methods=["PUT"])
@jwt_required
def edit_order(orderId):
    
    ''' This function uses the PUT method to update the order status of the order with that given orderId.
    it takes in an order id and searches for that order with that id and then returns an updated order '''
    data = request.get_json()
    status = data.get('status')

    updated_order = Order.update_status(orderId, status)
    return jsonify({"Updated order": updated_order,
                'message': 'Order status has been updated'}), 201