''' These are the imports for the required packages '''
from app.database.dbmanager import DatabaseConnection
import psycopg2.extras
from app import app
from app.validate import Validator
import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request, jsonify
from app.modules.meal_model import Meal
from app.modules.customer_model import Customer


@app.route("/api/v2/menu", methods=['POST'])
@jwt_required
def add_meal():

    ''' This function helps the administrator to add a meal through the POST method
        it takes in input data from the admin and
        posts the data into the database returning the meal added '''
    try:
        admin = get_jwt_identity()
        data = request.get_json()
        thetype = data.get('thetype')
        food = data.get('food')
        price = data.get('price')
        description = data.get('description')

        valid = Validator.validate_meal_inputs(data['thetype'], data['food'], data['price'], data['description'])
        '''Validating and checking for similar data'''
        if valid == True:
            admin = Customer(admin, None, None)
            admin_logged_in = admin.get_admin_credentials_by_username(admin)
            if admin_logged_in:
                meal_data = Meal(None, data['food'], None, None)
                same_data = meal_data.check_for_same_food_name()
                if same_data:
                    return jsonify({"message":"Meal already exists, place another"}), 400 
                '''Add the meal'''
                obj = Meal(thetype, food, price, description)
                result = obj.adding_meal()
                return result
            else:
                return jsonify({'message': 'Unauthorized access'}), 401
        else:
            return valid
    except:
        response = jsonify({"Error": "Some fields are missing, please check"})
        response.status_code = 400
        return response


@app.route("/api/v2/menu", methods=['GET'])
def get_all_meals():
    
    ''' This function routes to /api/v2/menu and uses the GET method to return all the added meals '''
    all_meals = Meal.get_all_meals()
    return jsonify({'All meals': all_meals,
                    'message': 'All meals have been viewed'}), 201
