from application import webapp
from flask import request, json, jsonify
from application.modules import Customer, Meal, Order
from validation.validate import Validate
from datetime import date


all_orders = []
all_meals = []

@webapp.route('/api/v1/meals', methods = ['POST'])
def add_meal():
    data = request.get_json()
    mealId = len(all_meals) + 1
    food = data.get('food')
    price = data.get('price')

    # if Validate.validate_empty

    new_meal = Meal(mealId, food, price)
    all_meals.append(new_meal) 
    return jsonify({'message': 'The meal has been successfully added'}), 200


@webapp.route('/api/v1/orders', methods = ['POST'])
def make_order(mealId):
    data = request.get_json()
    orderId = len(all_orders) + 1
    mealId = data.get('mealId')
    today = str(date.today())
        
    # for meal in all_meals:
    #     if mealId in meal:
    #         Order = Order
    #         new_order = Order(orderId, new_meal, today)
    #         all_orders.append(new_order)

    new_order = Order(orderId, today)
    all_orders.append(new_order)  
    
    return jsonify({'message': 'Order successfully made'}), 200    
