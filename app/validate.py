import re
from flask import jsonify


class Validator():

    @classmethod
    def validate_admin_inputs(cls, username, password):
        '''method to validate customer input'''
        if username == '':
            return jsonify({"message": "Username is missing"}), 400
        elif ' ' in username:
            return jsonify({"message": "Username should have no spaces"}), 400
        elif not re.search(r"\b[a-zA-Z]+\b", username):
            return jsonify({"message": "Username should be in characters"}), 400
        elif password == '':
            return jsonify({"message": "Password is missing"}), 400
        elif not re.search(r"^(?=.*[a-z])[a-z]{5}$", password):
            return jsonify({"message": "Password must have 5 characters with only lowercase letters"}), 400
        else:
            return True


    @classmethod
    def validate_registration_inputs(cls, username, contact, password):
        '''method to validate customer input'''
        if username == '':
            return jsonify({"message": "Username is missing"}), 400
        elif ' ' in username:
            return jsonify({"message": "Username should have no spaces"}), 400
        elif not re.search(r"\b[a-zA-Z]+\b", username):
            return jsonify({"message": "Username should be in characters"}), 400
        elif contact == '':
            return jsonify({"message": "Contact is missing"}), 400
        elif not re.search(r"^\+256[-]\d{3}[-]\d{6}$", contact):
            return jsonify({"message": "Contact should be like this format '+256-755-598090'"}), 400
        elif password == '':
            return jsonify({"message": "Password is missing"}), 400
        elif not re.search(r"^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{7}$", password):
            return jsonify({"message": "Password must have 7 characters with atleast a lowercase, uppercase letter and a number"}), 400
        else:
            return True

    
    @classmethod
    def validate_meal_inputs(cls, thetype, food, price, description):
        '''method to validate admin input'''
        if thetype == '':
            return jsonify({"message": "The type is missing"}), 400
        elif ' ' in thetype:
            return jsonify({"message": "The type of food should have no spaces"}), 400
        elif not re.search(r"\b[a-zA-Z]+\b", thetype):
            return jsonify({"message": "The type of food should be in characters"}), 400
        elif food == '':
            return jsonify({"message": "Food is missing"}), 400
        elif ' ' in food:
            return jsonify({"message": "The food should have no spaces"}), 400
        elif not re.search(r"\b[a-zA-Z]+\b", food):
            return jsonify({"message": "The food should be in characters"}), 400
        elif price == '':
            return jsonify({"message": "Price is missing"}), 400
        elif ' ' in price:
            return jsonify({"message": "The price should have no spaces"}), 400
        elif not re.search(r"\b[0-9]+\b", price):
            return jsonify({"message": "The price should be in numbers"}), 400
        elif description == '':
            return jsonify({"message": "Description is missing"}), 400
        elif not re.search(r"^([a-zA-Z]+\s)*[a-zA-Z]+$", description):
            return jsonify({"message": "The description should be in characters"}), 400
        else:
            return True


    @classmethod
    def validate_order_inputs(cls, food, quantity):
        '''method to validate my input'''
        if food == '':
            return jsonify({"message": "Food is missing"}), 400
        elif ' ' in food:
            return jsonify({"message": "The food should have no spaces"}), 400
        elif not re.search(r"\b[a-zA-Z]+\b", food):
            return jsonify({"message": "The food should be in characters"}), 400
        elif quantity == '':
            return jsonify({"message": "Quantity is missing"}), 400
        elif ' ' in quantity:
            return jsonify({"message": "The quantity should have no spaces"}), 400
        elif not re.search(r"\b[0-9]+\b", quantity):
            return jsonify({"message": "The quantity should be a number"}), 400
        else:
            return True
