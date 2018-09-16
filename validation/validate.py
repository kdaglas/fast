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
    def validate_input1(cls, thetype, food, price):

        # method to validate my input

        if thetype == '':
            return jsonify({"message": "The type of food is missing"}), 400
        elif not re.search("^[a-zA-Z]", thetype):
            return jsonify({"message": "The type of food should be in characters"}), 400
        elif food == '':
            return jsonify({"message": "The food is missing"}), 400
        elif not re.search("^[a-zA-Z]", food):
            return jsonify({"message": "The food should be in characters"}), 400
        elif price == '':
            return jsonify({"message": "The price is missing"}), 400
        elif not re.search("^[0-9]", price):
            return jsonify({"message": "The price should be in numbers"}), 400
        else:
            return True

    @classmethod
    def validate_input2(cls, food, quantity):

        # method to validate my input

        if food == '':
            return jsonify({"message": "The food is missing"}), 400
        elif not re.search("^[a-zA-Z]", food):
            return jsonify({"message": "The food should be in characters"}), 400
        elif quantity == '':
            return jsonify({"message": "The quantity is missing"}), 400
        elif not re.search("^[0-9]", quantity):
            return jsonify({"message": "The quantity should be a number"}), 400
        else:
            return True

    def validate_id(self, mealId):

        # valiation class for the meal id

        # try:
        #    mealId = int(mealId)
        # except ValueError:
        #     return jsonify({"message": "Id should be an interger"}), 400

        valid = ""
        if type(self.mealId) is not int:
            valid="The mealId should be an integer"     
        elif not re.search("^[0-9]" , self.mealId):
            valid="The mealId should be an integer"    
        else:
            valid = True
        return valid

    def validate_quantity(self, quantity):

        # valiation class for the quantity

        # try:
        #    quantity = int(quantity)
        # except ValueError:
        #     return jsonify({"message": "The quantity should be an interger"}), 400

        valid = ""
        if type(self.quantity) is not int:
            valid="The quantity should be an integer"     
        elif not re.search("^[0-9]" , self.quantity):
            valid="The quantity should be an integer"    
        else:
            valid = True
        return valid
        