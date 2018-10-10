''' These are the imports for the required packages '''
from app.database.dbmanager import DatabaseConnection
import psycopg2
from flask import jsonify
from app import app


@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the fastFoodfast app!'})
