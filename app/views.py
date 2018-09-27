''' These are the imports for the required packages '''

from app import app
from flask import request, json, jsonify
from app.modules.customer_model import Customer
from app.modules.order_model import Order
from app.validation.validate import Validate
from datetime import date
import uuid


@app.route("/api/v1/register", methods=['POST'])
def register():

    ''' This function registers a customer through POST method by taking in
        the input from the user and posting it to the server '''
    try:
        data = request.get_json()
        customerId = int(str(uuid.uuid1().int)[:5])
        username = data.get('username')
        emailaddress = data.get('emailaddress')
        contact = data.get('contact')
        password = data.get('password')

        valid = Validate.validate_registration_inputs(data['username'], data['emailaddress'], data['contact'], data['password'])

        if valid == True:
            new_customer = Customer(customerId, username, emailaddress, contact, password)
            registered_customer = Customer.register_customer(new_customer)
            return jsonify({'New customer':registered_customer,
                            'message': 'Customer has been registered'}), 201
        else:
            return valid
    except:
        response = jsonify({"message": "The key or value fields are invalid or missing"})
        response.status_code = 403
        return response 


@app.route("/api/v1/login", methods=['POST'])
def login():

    ''' This fuction through the POST method, logins in auser and returns that user and if
        the user is not found or doesnot exist then it returns 404 '''
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        valid = Validate.validate_login_inputs(data['username'], data['password'])

        if valid == True:
            customer = Customer.login(username, password)
            return jsonify({'Customer': customer,
                            'message': 'Customer has been logged in'}), 200
        else:
                return valid
    except:
        response = jsonify({"message": "The key or value fields are invalid or missing"})
        response.status_code = 403
        return response


@app.route("/api/v1/orders", methods=['POST'])
def place_order():

    ''' This function helps the customer to create or place an order through the POST method
        it takes in input data from the customer preferably the order to be made and
        posts the data returning the order made by the customer '''
    try:
        data = request.get_json()
        orderId = int(str(uuid.uuid1().int)[:5])
        customerId = data.get('customerId')
        today = str(date.today())
        food = data.get('food')
        thetype = data.get('thetype')
        price = data.get('price')
        quantity = data.get('quantity')
        status = 'not completed'

        valid = Validate.validate_order_input(data['customerId'], data['thetype'], data['food'], data['price'], data['quantity'])

        if valid == True:   
            new_order = Order(customerId, orderId, thetype, food, price, quantity, status, today)
            placed_order = Order.place_order(new_order)
            return jsonify({'Placed order': placed_order,
                            'message': 'Your order has been placed'}), 201
        else:
            return valid
    except:
        response = jsonify({"message": "The key or value fields are invalid or missing"})
        response.status_code = 403
        return response


@app.route("/api/v1/orders", methods=['GET'])
def get_all_orders():
    
    ''' This function routes to /api/v1/orders and uses the GET method to return all the orders made '''
    all_orders = Order.get_all_orders()
    return jsonify({'All your orders': all_orders,
                    'message': 'All orders have been viewed'}), 302


@app.route("/api/v1/orders/<orderId>", methods=["GET"])
def get_single_order(orderId):
    
    ''' This function routes to /api/v1/orders/<ordersId> and uses the GET method to return a particular order made
        it takes in the order id as its key search value so to return that particular order '''
    order = Order.get_one_order(orderId)
    return jsonify({"Your order": order,
                    'message': 'One order has been viewed'}), 302


@app.route("/api/v1/orders/<orderId>", methods=["PUT"])
def edit_order(orderId):
    
    ''' This function uses the PUT method to update the order status of the order with that given orderId.
    it takes in an order id and searches for that order with that id and then returns an updated order '''
    data = request.get_json()
    status = data.get('status')

    updated_order = Order.update_order(orderId, status)
    return jsonify({"Updated order": updated_order,
                'message': 'Order status has been updated'}), 201
