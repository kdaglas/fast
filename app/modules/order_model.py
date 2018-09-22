#  Object classes for the order model

all_orders = []

class Order():

    # initialising the order class
    def __init__(self, customerId, orderId, thetype, food, price, quantity, status, today):

        self.customerId = customerId
        self.orderId = orderId
        self.thetype = thetype
        self.food = food
        self.price = price
        self.quantity = quantity
        self.status = status
        self.today = today
    
    # method that gets the order class and makes it a dictionary
    def place_order(self):

        order = {
            'customerId' : self.customerId,
            'orderId' : self.orderId,
            'thetype' : self.thetype,
            'food' : self.food,
            'price' : self.price,
            'quantity' : self.quantity,
            'status' : 'Not covered',
            'today' : self.today
        }

        all_orders.append(order)
        return order

    # method to return the placed orders
    @classmethod
    def get_all_orders(cls):

        if len(all_orders) > 0:
            return [order for order in all_orders]
        return {'There is an error': 'No customers Found'}

    # method to return the one order
    @classmethod
    def get_one_order(cls, orderId):

        if int(orderId) > 0:
            if len(all_orders) > 0:
                for order in all_orders:
                    if order.get('orderId') == int(orderId):
                        return order

                return {"message": "order doesnot exist"}
            return {"message": "No order has been registered yet"}
        return {"message": "Single order id has to bigger than zero"}
        
    # method to return the edited order
    @classmethod
    def update_order(cls, orderId, status):

        for order in all_orders:
            if order.get('orderId') == int(orderId):
                order['status'] = status
                return order
        return {'There is an error': 'No order Found'}
