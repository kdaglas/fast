from application import webapp
from flask import request, json, jsonify
from modules.models import Meal, Order
from validation.validate import Validate
from datetime import date
import uuid


all_orders = []
all_meals = []

@webapp.route('/api/v1/meals', methods = ['POST'])
def add_meal():

    data = request.get_json()
    mealId = int(str(uuid.uuid1().int)[:10])
    # mealId = len(all_meals) + 1
    thetype = data.get('thetype')
    food = data.get('food')
    price = data.get('price')

    valid = Validate.validate_input1(data["thetype"], data["food"], data["price"])
    
    if valid == True:
        new_meal = Meal(mealId, thetype, food, price)
        all_meals.append(new_meal) 
        return jsonify({ 
            'This is the meal':new_meal.__dict__,
            'message':'Meal successfully added'}), 201 
    else:
        return valid


@webapp.route('/api/v1/meals', methods=['GET'])
def get_all_meals():

    if len(all_meals) > 0:
        return jsonify({'All the available meals are here': [
                            meal.__dict__ for meal in all_meals
                        ],
                        'message': 'All meals successfully viewed'
                        }), 200

    return jsonify({'message': 'No order made'}), 404


@webapp.route('/api/v1/orders', methods = ['POST'])
def make_order():

    data = request.get_json()
    orderId = int(str(uuid.uuid1().int)[:10])
    # orderId = len(all_orders) + 1
    # orderId = len(all_orders) + 1
    mealId = data.get('mealId')
    quantity = data.get('quantity')
    today = str(date.today())

    valids = Validate.validate_input2(data["mealId"], data["quantity"])
    
    if valids == True:
        # for meal in all_meals: # and mealId in meal:
        if mealId in meal for meal in all_meals:
            new_order = Order(orderId, mealId, meal.thetype, meal.food, meal.price, quantity, today) 
            return jsonify({ 
                'Your order is':new_order.__dict__,
                'message':'Order successfully made'}), 200
        return jsonify({ 
                'Your order is':new_order.__dict__,
                'message':'Meal id not found please input another'}), 404
    else:
        return valids


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
