class Customer():

    def __init__(self, userId, username, contact, password):
        self.userId = userId
        self.username = username
        self.contact = contact
        self.password = password


class Meal():

    def __init__(self, mealId, food, price):
        self.mealId = mealId
        self.food = food
        self.price = price


class Order(Meal):

    def __init__(self, orderId, mealId, food, price, today):
        Meal.__init__(self, mealId, food, price)
        self.orderId = orderId
        self.today = today