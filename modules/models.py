class Meal():

    def __init__(self, mealId, thetype, food, price):
        self.mealId = mealId
        self.thetype = thetype
        self.food = food
        self.price = price


class Order(Meal):

    def __init__(self, orderId, mealId, thetype, food, price, quantity, today):
        Meal.__init__(self, mealId, thetype, food, price)
        self.orderId = orderId
        self.quantity = quantity
        self.today = today