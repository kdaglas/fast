from app import app
from flask import request, json, jsonify
from app.modules.customer_model import Customer
from app.modules.order_model import Order
from app.validation.validate import Validate
from datetime import date
import uuid


@app.route("/api/v1/register", methods=['POST'])
def register():

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
    
    # if request.method == 'GET':
    all_orders = Order.get_all_orders()
    return jsonify({'All your orders': all_orders,
                    'message': 'All orders have been viewed'}), 302
    # else:
    #     return jsonify({'message': 'Bad request'}), 405


@app.route("/api/v1/orders/<orderId>", methods=["GET"])
def get_single_order(orderId):
    
    order = Order.get_one_order(orderId)
    return jsonify({"Your order": order,
                    'message': 'One order has been viewed'}), 302


@app.route("/api/v1/orders/<orderId>", methods=["PUT"])
def edit_order(orderId):
    
    data = request.get_json()
    status = data.get('status')

    updated_order = Order.update_order(orderId, status)
    return jsonify({"Updated order": updated_order,
                'message': 'Order status has been updated'}), 201
