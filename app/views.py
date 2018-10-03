''' These are the imports for the required packages '''
from app import app
import json
from flask import request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app.modules.customer_model import Customer
from app.modules.meal_model import Meal
from app.modules.order_model import Order
from datetime import date
from app.database.dbfuncs import DatabaseFunctions


@app.route("/api/v2/register", methods=['POST'])
def register():

    ''' This function registers a customer through POST method by taking in
        the input from the user and storing it in the database '''
    try:
        reg_info = request.get_json()
        username = reg_info.get("username")
        contact = reg_info.get("contact")
        password = reg_info.get("password")

        ''' a function that adds new user to the database'''
        Customer.register_customer(username, contact, password)
        new_customer = Customer(
            username = username,
            contact = contact,
            password = password
        )
        return jsonify({'Customer': new_customer.__dict__,
                        'message': 'Customer has been registered'}), 200
    except:
        response = jsonify({"message": "The key or value fields are invalid or missing"}), 403
        return response


@app.route("/api/v2/login", methods=['POST'])
def login():

    ''' This fuction through the POST method, logins in a user and returns that user and if
        the user is not found or doesnot exist then it returns 404 '''
    try:
        request_data = request.get_json()
        username = request_data.get('username')
        password = request_data.get('password')

        ''' an imported function that returns the username from the database'''
        customer = DatabaseFunctions.get_customer_by_username(username)
        if customer:
            customer_token = {}
            access_token = create_access_token(identity=username)
            customer_token["token"] = access_token
            return jsonify({'message': 'Customer has been login in',
                            'Token': customer_token}), 200
        else:
            response = jsonify({"message": "These credentials are invalid or missing"}), 403
            return response
    except:
        response = jsonify({"message": "The key or value fields are invalid or missing"})
        response.status_code = 403
        return response


@app.route("/api/v2/meals", methods=['POST'])
def add_meal():

    ''' This function helps the administrator to add a meal through the POST method
        it takes in input data from the admin and
        posts the data into the database returning the meal added '''
    # try:
    data = request.get_json()
    food = data.get('food')
    thetype = data.get('thetype')
    price = data.get('price')
    description = data.get('description')

    ''' this function adds a meal to the menu and then to the database'''
    Meal.adding_meal(thetype, food, price, description)
    added_meal = Meal(
        thetype = thetype,
        food = food,
        price = price,
        description = description
    )
    return jsonify({'Meal': added_meal.__dict__,
                    'message': 'Meal has been added'}), 200


@app.route("/api/v2/meals", methods=['GET'])
def get_all_meals():
    
    ''' This function routes to /api/v2/meals and uses the GET method to return all the added meals '''
    meals = Meal.get_all_meals()
    return jsonify({'All meals': meals,
                    'message': 'All meals have been viewed'}), 201


# @app.route("/api/v1/orders", methods=['POST'])
# def place_order():

#     ''' This function helps the customer to create or place an order through the POST method
#         it takes in input data from the customer preferably the order to be made and
#         posts the data returning the order made by the customer '''
#     try:
#         data = request.get_json()
#         customerId = data.get('customerId')
#         today = str(date.today())
#         food = data.get('food')
#         thetype = data.get('thetype')
#         price = data.get('price')
#         quantity = data.get('quantity')
#         status = 'not completed'
  
#         new_order = Order(customerId, orderId, thetype, food, price, quantity, status, today)
#         placed_order = Order.place_order(new_order)
#         return jsonify({'Placed order': placed_order,
#                         'message': 'Your order placed'}), 201
#     except:
#         response = jsonify({"message": "The key or value fields are invalid or missing"})
#         response.status_code = 403
#         return response


# @app.route("/api/v1/orders", methods=['GET'])
# def get_all_orders():
    
#     ''' This function routes to /api/v1/orders and uses the GET method to return all the orders made '''
#     all_orders = Order.get_all_orders()
#     return jsonify({'All your orders': all_orders,
#                     'message': 'All orders have been viewed'}), 302


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
