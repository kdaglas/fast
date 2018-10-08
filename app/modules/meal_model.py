from app.database.dbmanager import DatabaseConnection
import psycopg2
from flask import jsonify
from app import app


dbcon = DatabaseConnection()

'''Object classes for the meal model'''
class Meal():
    
    def __init__(self, thetype, food, price, description):
        '''Initialising the order class'''
        self.thetype = thetype
        self.food = food
        self.price = price
        self.description = description
    
    
    def adding_meal(self):
        '''this method returns a dictionary format of the meal class'''
        try:
            dbcon.cursor.execute("""INSERT INTO menu(thetype, food, price, description) VALUES (%s, %s, %s, %s)""",
                        (self.thetype, self.food, self.price, self.description))
            response = jsonify({"message": "The meal with {} has been added".format(self.food)})
            response.status_code = 201
            return response
        except:
            return jsonify({"message": "Unable to add a meal"})

        
    def check_for_same_food_name(self):
        '''method that if a food already exists in the database'''
        dbcon.cursor.execute("""SELECT food FROM menu WHERE food = %s""",(self.food,))
        rows = dbcon.cursor.fetchone()
        return rows

    
    def get_all_meals(self):
        '''this method returns the added meals'''
        dbcon.cursor.execute("""SELECT row_to_json(row) FROM (select * from menu) row""")
        all_meals = dbcon.cursor.fetchall()
        return all_meals

    
    def get_one_meal(self, mealId):
        '''This method returns the one meal'''
        pass

    
    def update_order(self, mealId, price):
        '''this method return the edited order'''
        # for meal in all_meals:
        #     if meal.get('mealId') == int(mealId):
        #         meal['price'] = price
        #         return meal
        # return {'There is an error': 'No meal Found'}
        pass
