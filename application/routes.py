from application import webapp
from flask import request, json, jsonify
from application.modules import Customer, Meal, Order
from datetime import date


all_customers = []
all_orders = []
all_meals = []

@webapp.route('/api/v1/meals', methods = ['POST'])
def add_meal():
    data = request.get_json()
    mealId = len(all_meals) + 1
    food = data.get('food')
    price = data.get('price')

    new_meal = Meal(mealId, food, price)
    all_meals.append(new_meal) 
    return jsonify({'message': 'The meal has been successfully added'}), 200


@webapp.route('/api/v1/orders', methods = ['POST'])
def make_order(mealId):
    data = request.get_json()
    orderId = len(all_orders) + 1
    mealId = data.get('mealId')
    today = str(date.today())
        
    for meal in all_meals:
        if mealId in meal:
            Order(Meal) = Order
            new_order = Order(orderId, new_meal, today)
            all_orders.append(new_order)  
    
    return jsonify({'message': 'Order successfully made'}), 200


    if len(meal) < 1:
        return jsonify({'message': 'Meal is missing'}), 400
    if len(price) < 1:
        return jsonify({'message': 'Price is missing'}), 400

    for order in all_orders:
        if order.order == order:
            return jsonify({'message':'Same order made'})
        
    
@webapp.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    if len(all_orders) > 0:
        return jsonify({'All orders are here': [
                            theorder.__dict__ for theorder in all_orders
                        ],
                        'message': 'All orders successfully viewed'
                        }), 200

    return jsonify({'message': 'No order made'}), 404
