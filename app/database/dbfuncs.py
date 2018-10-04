''' These are the imports for the required packages '''
from app.database.dbmanager import DatabaseConnection
from flask import jsonify
import psycopg2.extras


connect = DatabaseConnection()
cursor = connect.get_connection().cursor()

class DatabaseFunctions():
    '''Creating an interaction with the database'''
    # @staticmethod
    # def add_new_customer(username, contact, password):
    #     query = (
    #         """INSERT INTO customers (customerId, username, contact, password)
    #         VALUES (DEFAULT, '{}', '{}', '{}')
    #         RETURNING customerId, username, contact, password""".
    #         format(username, contact, password))
    #     cursor.execute(query)
    #     rows = cursor.fetchone()
    #     return rows


    @staticmethod
    def get_customer_by_id(customerId):
        query = (
            """SELECT * from customers where customerId = '{}'""".
            format(customerId))
        cursor.execute(query)
        rows = cursor.fetchone()
        return rows


    @staticmethod
    def get_customer_by_username(username):
        query = (
            """SELECT * from customers where username = '{}'""".
            format(username))
        cursor.execute(query)
        username = cursor.fetchone()
        return username


    @staticmethod
    def add_new_meal(thetype, food, price, description):
        query = (
            """INSERT INTO meals (mealId, thetype, food, price, description) 
            VALUES (DEFAULT, '{}', '{}', '{}', '{}')
            RETURNING mealId, thetype, food, price, description""".
            format(thetype, food, price, description))
        cursor.execute(query)
        rows = cursor.fetchone()
        return rows


    @staticmethod
    def get_meal_by_id(mealId):
        query = (
            # """SELECT * from meals where mealId = '{}'""".
            "SELECT row_to_json(row) FROM  (SELECT * from meals where mealId = '{}') row".
            format(mealId))
        cursor.execute(query)
        rows = cursor.fetchone()
        return rows


    @staticmethod
    def get_meal_by_food(food):
        query = (
            "SELECT * from meals where food = '{}'".
            # "SELECT row_to_json(row) FROM  (SELECT * from meals where food = '{}') row".
            format(food))
        cursor.execute(query)
        food = cursor.fetchone()
        return food


    @staticmethod
    def get_all_meals():
        query = (
            "SELECT row_to_json(row) FROM  (select * from meals) row"
        )
        cursor.execute(query) # SELECT row_to_json(row) FROM  (select * from users) row;
        all_meals = cursor.fetchall()
        return all_meals


    @staticmethod
    def get_single_meal(mealId):
        cursor = connect.get_connection().cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute("SELECT * FROM meals WHERE mealId = '{}'".
                    format(mealId))
        rows = cursor.fetchone()
        if not rows:
            return {"message": "Meal does not exist"}
        return rows


    @staticmethod
    def update_single_meal(mealId, price):
        cursor.execute("UPDATE meals SET price = '{}' WHERE mealId = '{}'".
                    format(price, mealId))
        rows = cursor.fetchone()
        if not rows:
            return {"message": "Meal not found"}
        return rows


    @staticmethod
    def delete_single_meal(mealId):
        cursor.execute("SELECT * FROM meals WHERE mealId = '{}'".
                    format(mealId))
        rows = cursor.fetchone()
        if rows:
            cursor.execute("DELETE FROM meals WHERE mealId = '{}'".
                    format(mealId))
            return jsonify({"message": "Meal has been deleted"})           
        else:
            return jsonify({"message": "Meal not found"})


    @staticmethod
    def place_new_order(customerId, mealId, quantity, status, today):
        query = (
            """INSERT INTO orders (orderId, customerId, mealId, quantity, status, today) 
            VALUES (DEFAULT, '{}', '{}', '{}', '{}', '{}')
            RETURNING orderId, customerId, mealId, quantity, status, today""".
            format(customerId, mealId, quantity, status, today))
        cursor.execute(query)
        rows = cursor.fetchone()
        return rows


    @staticmethod
    def get_all_orders():
        query = (
            "SELECT row_to_json(row) FROM  (select * from orders) row"
        )
        cursor.execute(query) # SELECT row_to_json(row) FROM  (select * from users) row;
        all_orders = cursor.fetchall()
        return all_orders


    @staticmethod
    def get_order_by_id(orderId):
        query = (
            # """SELECT * from meals where mealId = '{}'""".
            "SELECT row_to_json(row) FROM  (SELECT * from orders where orderId = '{}') row".
            format(orderId))
        cursor.execute(query)
        rows = cursor.fetchone()
        return rows


    # def update_single_entry(entry_id, title, content):
    #     if get_single_entry(entry_id)["message"] == "Entry does not exist":
    #         return "not found"
    #     else:
    #         cursor.execute("UPDATE entries SET title = %s, content = %s WHERE entry_id = %s",
    #                         (title, content, entry_id))
    #         return 'Entry edited'
