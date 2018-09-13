class Customer():

    def __init__(self, user_id, username, contact, password):
        self.user_id = user_id
        self.username = username
        self.contact = contact
        self.password = password


class Meal():

    def __init__(self, meal_id, meal, price):
        self.meal_id = meal_id
        self.meal = meal
        self.price = price


class Order(Meal):

    def __init__(self, order_id, meal_id, meal, price, today):
        Meal.__init__(self, meal_id, meal, price)
        self.order_id = order_id
        self.today = today