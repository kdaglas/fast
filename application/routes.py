from application import webapp
from flask import request, json, jsonify
from modules.models import Meal, Order
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

    new_meal = Meal(mealId, food, price)
    all_meals.append(new_meal) 
    return jsonify({ 
        'This is the meal':new_meal.__dict__,
        'message':'Meal successfully added'}), 200 


@webapp.route('/api/v1/orders', methods = ['POST'])
def make_order():
    data = request.get_json()
    orderId = len(all_orders) + 1
    mealId = data.get('mealId')
    today = str(date.today())
        
    for meal in all_meals:
        new_order = Order(orderId, mealId, meal.food, meal.price, today) 
        return jsonify({ 
            'Your order is':new_order.__dict__,
            'message':'Order successfully made'}), 200    
