import unittest
import json
from flask_jwt_extended import create_access_token
from app import app
from app.database.dbmanager import DatabaseConnection


dbcon = DatabaseConnection()

class Testing(unittest.TestCase):
    '''checking the api endpoints or routes'''
    wrong_fields = json.dumps(dict(user="Douglas", contact="+256-755-598090", password="Callme2"))
    same_contact = json.dumps(dict(user="Mike", contact="+256-755-598090", password="Mikee25"))
    register_customer = json.dumps(dict(username="Douglas", contact="+256-755-598090", password="Callme2"))
    same_customer = json.dumps(dict(username="Douglas", contact="+256-755-598090", password="Callme2"))
    invalid_customer = json.dumps(dict(username="1234", contact="+256-755-598090", password="Callme2"))
    wrong_contact = json.dumps(dict(username="Douglas", contact="+256-755598090", password="Callme2"))
    wrong_username = json.dumps(dict(username="***", contact="+256-755-598090", password="Callme2"))
    wrong_password = json.dumps(dict(username="Douglas", contact="+256-755-598090", password="Call2"))
    empty_contact = json.dumps(dict(username="Douglas", contact="", password="Callme2"))
    empty_username = json.dumps(dict(username="", contact="+256-755-598090", password="Callme2"))
    empty_password = json.dumps(dict(username="Douglas", contact="+256-755-598090", password=""))

    login_info = json.dumps(dict(username="Douglas", password="Callme2"))
    login_validation = json.dumps(dict(username="******", password="Callme2"))
    login_with_empty = json.dumps(dict(username="******", password="Callme2"))

    wrong_menu_fields = json.dumps(dict(thet="Breakfast", food="bans", price="2000", description="with milk"))
    same_food = json.dumps(dict(thetype="Breakfast", food="bans", price="2000", description="with milk"))
    add_meal = json.dumps(dict(thetype="Breakfast", food="bans", price="2000", description="with milk"))

    def setUp(self):
        """Making sure that you are in the right environment variable."""
        app.config['TESTING'] = True
        dbcon.create_tables()
        self.app = app
        with app.test_request_context():
            self.loggedin_user = dict(customerId=1, username='Douglas')
            self.access_token = create_access_token(self.loggedin_user)
            self.access_header = {'Authorization': 'Bearer {}'.format(
                                    self.access_token)}

    def tearDown(self):
        # customers = ("""DROP TABLE IF EXISTS customers CASCADE;""")
        # meals = ("""DROP TABLE IF EXISTS meals CASCADE;""")
        # orders = ("""DROP TABLE IF EXISTS orders CASCADE;""")
        # con = DatabaseConnection.delete_tables(self)
        # cursor = con.cursor()
        # cursor.execute(customers)
        # con.commit()
        # cursor.execute(orders)
        # con.commit()
        # cursor.execute(meals)
        # con.commit()
        dbcon.delete_tables()

if __name__ == '__main__':
    unittest.main()
