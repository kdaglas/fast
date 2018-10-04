import unittest
import json
from flask_jwt_extended import create_access_token
from app import app
from app.database.dbmanager import DatabaseConnection


class Testing(unittest.TestCase):
    '''checking the api endpoints or routes'''
    register_customer = json.dumps(dict(username="Douglas", contact="+256-755-598090", password="Callme2"))
    same_customer = json.dumps(dict(username="Douglas", contact="+256-755-598090", password="Callme2"))
    invaliduser = json.dumps(dict(username="1234", contact="+256-755-598090", password="Callme2"))
    wrong_contact = json.dumps(dict(username="Douglas", contact="+256-755598090", password="Callme2"))
    wrong_username = json.dumps(dict(username="***", contact="+256-755-598090", password="Callme2"))
    wrong_password = json.dumps(dict(username="Douglas", contact="+256-755-598090", password="Call2"))


    login_info = json.dumps(dict(username="Douglas", password="Callme2"))
    login_validation = json.dumps(dict(username="******", password="Callme2"))

    def setUp(self):
        """Make sure that you are in the right environment variable."""
        app.config['TESTING'] = True
        self.app = app
        with app.test_request_context():
            self.loggedin_user = dict(customerId=1, username='Douglas')
            self.access_token = create_access_token(self.loggedin_user)
            self.access_header = {'Authorization': 'Bearer {}'.format(
                self.access_token)}

    def tearDown(self):
        customers = ("""DROP TABLE IF EXISTS customers CASCADE;""")
        meals = ("""DROP TABLE IF EXISTS meals CASCADE;""")
        orders = ("""DROP TABLE IF EXISTS orders CASCADE;""")
        con = DatabaseConnection.delete_tables()
        cursor = con.cursor()
        cursor.execute(customers)
        con.commit()
        cursor.execute(orders)
        con.commit()
        cursor.execute(meals)
        con.commit()

if __name__ == '__main__':
    unittest.main()
