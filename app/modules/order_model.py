from app.database.dbmanager import DatabaseConnection
import psycopg2
import psycopg2.extras as dictionary
from flask import jsonify
from app import app


dbcon = DatabaseConnection()

'''Object classes for the order model'''
class Order():
    
    def __init__(self, customerId, mealId, quantity, status):
        '''Initialising the order class'''
        self.customerId = customerId
        self.mealId = mealId
        self.quantity = quantity
        self.status = status
    
    
    def place_order(self):
        '''this method adds the made order to the database'''
        try:
            dbcon.cursor.execute("""INSERT INTO orders(customerId, mealId, quantity, status) VALUES (%s, %s, %s, %s)""",
                        (self.customerId, self.mealId, self.quantity, self.status))
            response = jsonify({"message": "The order has been added"})
            response.status_code = 201
            return response
        except:
            return "Unable to place order"


    @staticmethod
    def check_and_return_food(food):
        '''method that returns the food in the database'''
        dbcon.cursor.execute("""SELECT * FROM menu WHERE food = %s""",(food,))
        food = dbcon.cursor.fetchone()
        return food


    @staticmethod
    def check_and_return_mealId(mealId):
        '''method that returns the mealId in the database'''
        dbcon.cursor.execute("""SELECT * FROM menu WHERE mealId = %s""",(mealId,))
        mealId = dbcon.cursor.fetchone()
        return mealId


    def check_for_same_order(self):
        '''method that checks if order already exists in the database'''
        dbcon.cursor.execute("""SELECT mealId FROM orders WHERE mealId = %s""",(self.mealId,))
        rows = dbcon.cursor.fetchone()
        return rows


    @staticmethod
    def get_food_by_id(mealId):
        '''method that checks if order already exists in the database'''
        dbcon.cursor.execute("""SELECT * FROM orders WHERE mealId = %s""", (mealId,))
        orders = dbcon.cursor.fetchone()
        return orders


    @staticmethod
    def get_order_by_id(orderId):
        '''method that checks if order already exists in the database'''
        dbcon.cursor.execute("""SELECT * FROM orders WHERE orderId = %s""", (orderId,))
        order = dbcon.cursor.fetchone()
        return order


    @staticmethod
    def get_all_orders():
        '''this method returns the placed orders'''
        try:
            dbcon.cursor.execute("""SELECT * FROM orders""")
            # dbcon.cursor.execute("""SELECT  order.orderId, order.quantity, order.status, order.today,
            #             meal.thetype, meal.food, meal.price, meal.description, customer.username from orders as order JOIN menu 
            #             as meal ON order.mealId = meal.mealId JOIN customers as customer ON order.customerId = customer.customerId""")
            all_orders = dbcon.cursor.fetchall()
            return all_orders
        except:
            return "Unable to get all orders"


    @staticmethod
    def update_status(status, orderId):
        '''this method returns the updated status'''
        dbcon.cursor.execute("""UPDATE orders SET status = %s WHERE orderId = %s""", (orderId, status))
        orders = dbcon.cursor.fetchone()
        updated_order = dbcon.cursor.rowcount
        print(updated_order)
        return updated_order

    # @staticmethod
    # def placing_order(customerId, mealId, quantity, status, today):
    #     '''this method returns a dictionary format of the meal class'''
    #     DatabaseFunctions.place_new_order(
    #         customerId = customerId,
    #         mealId = mealId,
    #         quantity = quantity,
    #         status = 'Pending',
    #         today = today
    #     )
    
    # @classmethod
    # def get_all_orders(cls):
    #     '''this method returns the placed orders'''
    #     if len(all_orders) > 0:
    #         return [order for order in all_orders]
    #     return {'There is an error': 'No orders found'}

    
    # @classmethod
    # def get_one_order(cls, orderId):
    #     '''This method returns the one order'''
    #     if int(orderId) > 0:
    #         if len(all_orders) > 0:
    #             for order in all_orders:
    #                 if order.get('orderId') == int(orderId):
    #                     return order
    #             return {"message": "order doesnot exist"}
    #         return {"message": "No order has been registered yet"}
    #     return {"message": "Order id has to bigger than zero"}
        
    
    # @classmethod
    # def update_order(cls, orderId, status):
    #     '''this method return the edited order'''
    #     for order in all_orders:
    #         if order.get('orderId') == int(orderId):
    #             order['status'] = status
    #             return order
    #     return {'There is an error': 'No order Found'}
