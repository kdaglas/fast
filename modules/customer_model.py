all_customers = []

class Customer():

    def __init__(self, customerId, username, contact, password):

        # initialising the customer class

        self.customerId = customerId
        self.username = username
        self.contact = contact
        self.password = password

    def register_customer(self):

        # method that gets the order class and makes it a dictionary

        customer = {
            'customerId' : self.customerId,
            'username' : self.username,
            'contact' : self.contact,
            'password' : self.password
        }

        all_customers.append(customer)
        return customer

    def get_all_customers(self):

        # method that gets all the customers who have registered

        if all_customers:
            return all_customers
        return {'There is an error': 'No customers Found'}

    def get_a_customer(self, customerId):

        # method that gets all the customers who have registered

        for customer in all_customers:
            if customer.get('customerId') == customerId:
                return customer
        return {'There is an error': 'No customers Found'}
