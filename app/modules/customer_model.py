from app.database.dbfuncs import DatabaseFunctions

'''Object classes for the customer model'''
all_customers = []

class Customer():

    def __init__(self, username, contact, password):
        '''Initialise all params'''
        self.username = username
        self.contact = contact
        self.password = password

    @staticmethod
    def register_customer(username, contact, password):
        '''method that returns the customer class as a dictionary'''
        # DatabaseFunctions.add_new_customer(username, contact, password)
        DatabaseFunctions.add_new_customer(
            username = username,
            contact = contact,
            password = password
        )
    

    def get_all_customers(self):
        '''method that gets all the customers who have registered'''
        if all_customers:
            return all_customers
        return {'There is an error': 'No customers Found'}

    
    @classmethod
    def login(cls, username, password):
        '''method that logs in the customer who is registered'''
        for customer in all_customers:
            if customer.get('username') == username:
                return customer
        return {'There is an error': 'No customers Found'}
