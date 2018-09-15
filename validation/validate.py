import re
from flask import jsonify


class Validate():

    def __init__(self, thetype, food, price):

        # valiation class for the meal inputs

        self.thetype = thetype
        self.food = food
        self.price = price

    def validate_empty(self):

        # method to validate my input

        if not self.food:
            return jsonify({"message": "The food type is missing"}), 400
        elif not re.search("^[a-zA-Z]", self.food):
            return jsonify({"message": "The food type should be characters"}), 400

        if not self.price:
            return jsonify({"message": "The price is missing"}), 400
        elif not re.search("^[0-9]", self.price):
            return jsonify({"message": "The price should be numbers"}), 400

    def validate_id(self, mealId):

        # valiation class for the meal id

        try:
           mealId = int(mealId)
        except ValueError:
            return jsonify({"message": "Id should be an interger"}), 400

    def validate_quantity(self, quantity):

        # valiation class for the quantity

        try:
           quantity = int(quantity)
        except ValueError:
            return jsonify({"message": "The quantity should be an interger"}), 400
        