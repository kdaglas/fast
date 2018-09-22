#  Object classes for the customer model """
all_customers = []

class Customer():

    # Initialise all params
    def __init__(self, customerId, username, emailaddress, contact, password):
        self.customerId = customerId
        self.username = username
        self.emailaddress = emailaddress
        self.contact = contact
        self.password = password

    # method that gets the customer class and makes it a dictionary
    def register_customer(self):

        customer = {
            'customerId' : self.customerId,
            'username' : self.username,
            'emailaddress' : self.emailaddress,
            'contact' : self.contact,
            'password' : self.password
        }

        all_customers.append(customer)
        return customer

    # method that gets all the customers who have registered
    def get_all_customers(self):

        if all_customers:
            return all_customers
        return {'There is an error': 'No customers Found'}

    # method that logs in the customer who is registered
    @classmethod
    def login(cls, username, password):

        for customer in all_customers:
            if customer.get('username') == username and customer.get('password'):
                return customer
        return {'There is an error': 'No customers Found'}
        
