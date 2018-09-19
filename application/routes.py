from application import webapp
from flask import request, json, jsonify
from modules.customer_model import Customer
from modules.order_model import Order
from validation.validate import Validate
from datetime import date
import uuid


@webapp.route('/api/v1/register', methods=['POST'])
def register():

    try:
        data = request.get_json()
        customerId = int(str(uuid.uuid1().int)[:10])
        username = data.get('username')
        contact = data.get('contact')
        password = data.get('password')

        valid = Validate.validate_registration_inputs(data['username'], data['contact'], data['password'])
        
        if valid == True:
            new_customer = Customer(customerId, username, contact, password)
            registered_customer = Customer.register_customer(new_customer)
            return jsonify({'New customer':registered_customer,
                            'message': 'Customer successfully registered'}), 201 
        else:
            return valid

    except:
        response = jsonify({"message": "The key or value fields are invalid or are missing"})
        response.status_code = 400
        return response


@webapp.route('/api/v1/orders', methods = ['POST'])
def place_order():

    try:
        data = request.get_json()
        customerId = data.get('customerId')
        orderId = int(str(uuid.uuid1().int)[:10])
        thetype = data.get('thetype')
        food = data.get('food')
        price = data.get('price')
        quantity = data.get('quantity')
        today = str(date.today())

        valid = Validate.validate_order_input(data['customerId'], data['thetype'], data['food'], data['price'], data['quantity'])
        
        if valid == True:
            new_order = Order(customerId, orderId, thetype, food, price, quantity, today)
            placed_order = Order.place_order(new_order)
            return jsonify({'You have placed this order': placed_order,
                            'message': 'Your order has been successfully placed'}), 200
        else:
            return valid

    except:
        response = jsonify({"message": "The key or value fields are invalid or missing"})
        response.status_code = 400
        return response


@webapp.route('/api/v1/orders', methods=['GET'])
def get_all_orders():

    all_orders = Order.get_all_orders()
    return jsonify({'All your orders are here': all_orders,
                    'message': 'All your orders successfully viewed'}), 200


@webapp.route('/api/v1/orders/<orderId>', methods=['GET'])
def get_single_order(orderId):

    order = Order.get_one_order(orderId)
    if type(order) == str:
        return order, 400
    return jsonify({"This is your order": order,
                    'message': 'Your one order successfully viewed'}), 200


# @webapp.route('/api/v1/orders/<orderId>', methods=['PUT'])
# def edit_order(orderId):

#     data = request.get_json()
#     new_order = {}
#     # new_order['customerId'] = data.get('customerId')
#     new_order['thetype'] = data.get('thetype')
#     new_order['food'] = data.get('food')
#     new_order['price'] = data.get('price')
#     new_order['quantity'] = data.get('quantity')

#     edited_order = Order.update_order(orderId, thetype, food, price, quantity, today)
#     return jsonify({"Your edited order is": edited_order,
#                     'message': 'Your one order successfully updated'}), 200
