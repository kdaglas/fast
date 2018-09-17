class Customer():

    def __init__(self, customerId, username, contact, password):
        self.customerId = customerId
        self.username = username
        self.contact = contact
        self.password = password


class Order():

    def __init__(self, orderId, thetype, food, price, quantity, today):
        self.orderId = orderId
        self.thetype = thetype
        self.food = food
        self.price = price
        self.quantity = quantity
        self.today = today
