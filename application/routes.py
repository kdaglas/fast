from application import webapp
from flask import request, json, jsonify
from modules.models import Customer, Order
from validation.validate import Validate
from datetime import date
import uuid


all_customers = []
all_orders = []


@webapp.route("/api/v1/register", methods=['POST'])
def register():
    data = request.get_json()
    customerId = int(str(uuid.uuid1().int)[:10])
    username = data.get('username')
    contact = data.get('contact')
    password = data.get('password')

    valid = Validate.validate_registration_inputs(data["username"], data["contact"], data["password"])
    
    if valid == True:
        new_customer = Customer(customerId, username, contact, password)
        all_customers.append(new_customer)
        return jsonify({'message': 'Customer successfully registered'}), 201 
    else:
        return valid


@webapp.route("/api/v1/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    valid = Validate.validate_login_input(data["username"], data["password"])
    
    if valid == True:
        # if username in all_customers and password in all_customers: 
        return jsonify({'message': 'Successfully logged in'}), 201 
    else:
        return valid


@webapp.route('/api/v1/orders', methods = ['POST'])
def place_order():

    data = request.get_json()
    orderId = int(str(uuid.uuid1().int)[:10])
    thetype = data.get('thetype')
    food = data.get('food')
    price = data.get('price')
    quantity = data.get('quantity')
    today = str(date.today())

    valid = Validate.validate_order_input(data["thetype"], data["food"], data["price"], data["quantity"])
    
    if valid == True:
        new_order = Order(orderId, thetype, food, price, quantity, today)
        all_orders.append(new_order) 
        return jsonify({ 
            'This is your order':new_order.__dict__,
            'message':'Order successfully placed'}), 201 
    else:
        return valid


@webapp.route('/api/v1/orders', methods=['GET'])
def get_all_orders():

    if len(all_orders) > 0:
        return jsonify({'All the orders are here': [
                            order.__dict__ for order in all_orders
                        ],
                        'message': 'All orders successfully viewed'
                        }), 200

    return jsonify({'message': 'No order made'}), 404


@webapp.route('/api/v1/orders/<orderId>', methods=['GET'])
def get_single_order(orderId):

    if int(orderId) > 0:
        if len(all_orders) > 0:
            for order in all_orders:
                if order.orderId == int(orderId):
                    return jsonify({
                        'This is the order': order.__dict__,
                        'message': 'Single order successfully viewed'
                    }), 200

                return jsonify({'message': 'Order does not exist'}), 404
        return jsonify({'message': 'No order has been made yet'}), 404
    return jsonify({'message': 'Please type in an id greater than 0'}), 404


@webapp.route('/api/v1/orders/<orderId>', methods=['PUT'])
def edit_order(orderId):

    data = request.get_json()
    new_order = {}
    new_order['meal'] = data.get('meal')
    new_order['price'] = data.get('price')

    if int(orderId) > 0:
        if len(all_orders) > 0:    
            for order in all_orders:
                if order.orderId == int(orderId):
                    order.meal = new_order['meal']
                    order.price = new_order['price']
                    return jsonify({
                        'This is the new order': order.__dict__,
                        'message': 'Order has been modified'
                    }), 200

                return jsonify({'message': 'Order does not exist'}), 404
        return jsonify({'message': 'No order has been made yet'}), 404
    return jsonify({'message': 'Single order id has to be bigger than zero'}), 404
