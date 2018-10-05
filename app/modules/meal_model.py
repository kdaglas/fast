from app.database.dbmanager import DatabaseConnection
import psycopg2
from flask import jsonify
from app import app

class Meal():
    
    def __init__(self):
        '''Initialising the order class'''
        # self.thetype = thetype
        # self.food = food
        # self.price = price
        # self.description = description
    
    
    def adding_meal(self, thetype, food, price, description):
        '''this method returns a dictionary format of the meal class'''
        cursor = self.con.cursor()
        self.cursor.execute("""INSERT INTO meals(thetype, food, price, description) VALUES (%s, %s, %s, %s)""",
                    (self.thetype, self.food, self.price, self.description))
        self.con.commit()
        response = jsonify({"message": "Meal has been added"})
        response.status_code = 201
        return response
        

    def check_for_same_meal(self, food):
        '''method that if a food already exists in the database'''
        # cursor = self.con.cursor()
        cursor.execute("""SELECT food FROM meals WHERE food = %s""",(food,))
        rows = cursor.fetchone()
        return rows

    
    def get_all_the_meals(self):
        '''this method returns the added meals'''
        # return DatabaseFunctions.get_all_meals()
        query = ("SELECT row_to_json(row) FROM  (select * from meals) row"
        )
        self.cursor.execute(query) # SELECT row_to_json(row) FROM  (select * from users) row;
        all_meals = cursor.fetchall()
        return all_meals

    
    @classmethod
    def get_one_meal(cls, mealId):
        '''This method returns the one meal'''
        # if int(mealId) > 0:
        #     if len(all_meals) > 0:
        #         for meal in all_meals:
        #             if meal.get('mealId') == int(mealId):
        #                 return meal
        #         return {"message": "meal doesnot exist"}
        #     return {"message": "No meal has been registered yet"}
        # # return {"message": "Meal id has to bigger than zero"}
        # return DatabaseFunctions.get_meal_by_id(mealId)
        pass


        
    
    # @classmethod
    # def update_order(cls, mealId, price):
    #     '''this method return the edited order'''
    #     for meal in all_meals:
    #         if meal.get('mealId') == int(mealId):
    #             meal['price'] = price
    #             return meal
    #     return {'There is an error': 'No meal Found'}
