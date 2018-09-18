import re
from flask import jsonify


class Validate():

    def __init__(self, mealId, thetype, food, price, quantity):

        # valiation class for the meal inputs

        self.mealId = mealId
        self.thetype = thetype
        self.food = food
        self.price = price
        self.quantity = quantity


    @classmethod
    def validate_registration_inputs(cls, username, contact, password):

        # method to validate customer input

        if username == '':
            return jsonify({"message": "Your username is missing"}), 400
        elif ' ' in username:
            return jsonify({"message": "Your username should be have no spaces"}), 400
        elif not re.search("^[a-zA-Z]", username):
            return jsonify({"message": "Your username should be in characters"}), 400
        elif contact == '':
            return jsonify({"message": "Your contact is missing"}), 400
        elif not re.search(r"^\+256[-]\d{3}[-]\d{6}$", contact):
            return jsonify({"message": "Your contact should be in this format +256-755-598090"}), 400
        elif password == '':
            return jsonify({"message": "Your password is missing"}), 400
        elif not re.search(r"^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{7,}$", password):
            return jsonify({"message": "Your password must have 7 characters with atleast a lowercase and uppercase letter and 1 number"}), 400
        else:
            return True 


    @classmethod
    def validate_login_input(cls, username, password):

        # method to validate the customer input

        if username == '':
            return jsonify({"message": "Your username is missing"}), 400
        elif not re.search("^[a-zA-Z]", username):
            return jsonify({"message": "Your username should be in characters"}), 400
        elif password == '':
            return jsonify({"message": "Your password is missing"}), 400
        elif not re.search(r"^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{7,}$", password):
            return jsonify({"message": "Your password must have 7 characters with atleast a lowercase and uppercase letter and 1 number"}), 400
        else:
            return True 


    @classmethod
    def validate_order_input(cls, customerId, thetype, food, price, quantity):

        # method to validate my input

        if customerId == '':
            return jsonify({"message": "The customer's id is missing"}), 400
        # elif not re.search(r"\d", customerId):
        #     return jsonify({"message": "The customer's id should be a number"}), 400
        elif thetype == '':
            return jsonify({"message": "The type of food is missing"}), 400
        # elif not re.search("^[a-zA-Z]", thetype):
        #     return jsonify({"message": "The type of food should be in characters"}), 400
        elif food == '':
            return jsonify({"message": "The food is missing"}), 400
        # elif not re.search("^[a-zA-Z]", food):
        #     return jsonify({"message": "The food should be in characters"}), 400
        elif price == '':
            return jsonify({"message": "The price is missing"}), 400
        # elif not re.search("^[0-9]", price):
        #     return jsonify({"message": "The price should be in numbers"}), 400
        elif quantity == '':
            return jsonify({"message": "The quantity is missing"}), 400
        # elif not re.search("^[0-9]", quantity):
        #     return jsonify({"message": "The quantity should be a number"}), 400
        else:
            return True
        