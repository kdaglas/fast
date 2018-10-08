from app.database.dbmanager import DatabaseConnection
import psycopg2.extras
from app import app
from app.validate import Validator
import json
from flask import request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app.modules.meal_model import Meal

db = DatabaseConnection()

@app.route("/api/v2/menu", methods=['POST'])
def add_meal():

    ''' This function helps the administrator to add a meal through the POST method
        it takes in input data from the admin and
        posts the data into the database returning the meal added '''
    try:
        data = request.get_json()
        thetype = data.get('thetype')
        food = data.get('food')
        price = data.get('price')
        description = data.get('description')

        valid = Validator.validate_meal_inputs(data['thetype'], data['food'], data['price'], data['description'])
        '''Validating and checking for similar data'''
        if valid == True:
            meal_data = Meal(None, data['food'], None, None)
            same_data = meal_data.check_for_same_food_name()
            if same_data:
                return jsonify({"message":"Meal already exists, place another"}), 400 
            '''Add the meal'''
            obj = Meal(thetype, food, price, description)
            result = obj.adding_meal()
            return result
        else:
            return valid
    except:
        response = jsonify({"Error": "Some fields are missing, please check"})
        response.status_code = 403
        return response


# @app.route("/api/v2/menu", methods=['GET'])
# def get_all_meals():
    
#     ''' This function routes to /api/v2/menu and uses the GET method to return all the added meals '''
#     #obj = Meal(thetype, food, price, description)
#     all_meals = meal_data.get_all_the_meals()
#     return jsonify({'All meals': meals.__dict__,
#                     'message': 'All meals have been viewed'}), 201
#     ''' This function routes to /api/v2/meals and uses the GET method to return all the added meals '''
#     # meals = Meal.get_all_the_meals()
#     # return jsonify({'All meals': meals,
#     #                 'message': 'All meals have been viewed'}), 201
#     return jsonify({'message':db.get_all_meals()}),200


# @app.route("/api/v2/menu/<mealId>", methods=['GET'])
# def get_one_meal(mealId):
    
#     ''' This function routes to /api/v2/meals/<mealId> and uses the GET method to return a single meal '''
#     meal = Meal.get_one_meal(mealId)
#     return jsonify({'All meals': meal,
#                     'message': 'Meal has been viewed'}), 201