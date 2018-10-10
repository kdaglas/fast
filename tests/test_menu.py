from tests.test_base import Testing
from app import app
from app.database.dbmanager import DatabaseConnection
import json


dbcon = DatabaseConnection()

class MenuTests(Testing):

    def setUp(self):
        self.app = app.test_client()
        dbcon.create_tables()


    def test_add_meal_with_invalid_fields(self):
        '''test sdd a meal with invalid fields'''
        response = self.app.post('/api/v2/menu', data = Testing.wrong_menu_fields,
                                content_type="application/json")
        self.assertEqual(response.status_code, 401)
        self.assertIn(b"Some fields are missing, please check", response.data)


    def test_add_meal_with_same_food_name(self):
        '''test add a meal with same food'''
        response = self.app.post('/api/v2/menu', data = Testing.same_food,
                                content_type="application/json")
        self.assertEqual(response.status_code, 400)


    def test_add_meal(self):
        '''test sdd a meal with invalid fields'''
        response = self.app.post('/api/v2/menu', data = Testing.add_meal,
                                content_type="application/json")
        self.assertEqual(response.status_code, 401)
        self.assertIn(b"Some fields are missing, please check", response.data)