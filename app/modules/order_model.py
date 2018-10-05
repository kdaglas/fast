# from app.database.dbfuncs import DatabaseFunctions

'''Object classes for the order model'''

class Order():
    
    def __init__(self, customerId, mealId, quantity, status,today):
        '''Initialising the order class'''
        self.customerId = customerId
        self.mealId = mealId
        self.quantity = quantity
        self.status = status
        self.today = today
    

    @staticmethod
    def placing_order(customerId, mealId, quantity, status, today):
        '''this method returns a dictionary format of the meal class'''
        DatabaseFunctions.place_new_order(
            customerId = customerId,
            mealId = mealId,
            quantity = quantity,
            status = 'Pending',
            today = today
        )
    
    @classmethod
    def getting_all_orders(cls):
        '''this method returns the placed orders'''
        return DatabaseFunctions.get_all_orders()


    @classmethod
    def get_one_order(cls, orderId):
        '''This method returns the one meal'''
        return DatabaseFunctions.get_order_by_id(orderId)

    
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
