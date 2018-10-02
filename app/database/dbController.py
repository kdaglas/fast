import psycopg2
from app import app


class DatabaseConnection:

    def __init__(self):
        '''This constructor creates a connection to the database'''
        if app.config['TESTING']:
            print("Testing")
            self.con = psycopg2.connect(database="testdb", user="postgres",
                                        password="admin", host="localhost",
                                        port="5432"
                                        )
        else:
            print("Development")
            self.con = psycopg2.connect(database="fastFoodfastdb", user="postgres",
                                        password="admin", host="localhost",
                                        port="5432"
                                        )
        self.con.autocommit = True
        self.cursor = self.con.cursor()


    def get_connection(self):
        '''This function creates a connection to the database'''
        return self.con

    
    def create_tables(self):
        '''This function creates the tables'''
        queries = (
            """
            CREATE TABLE IF NOT EXISTS customers (
                customerId SERIAL PRIMARY KEY,
                username VARCHAR(25) NOT NULL UNIQUE,
                emailaddress VARCHAR(50) NOT NULL UNIQUE,
                contact VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(25) NOT NULL
            );
            """,

            """
            CREATE TABLE IF NOT EXISTS meals (
                mealId SERIAL PRIMARY KEY,
                thetype VARCHAR(50) NOT NULL,
                food VARCHAR(50) NOT NULL UNIQUE,
                price VARCHAR(100) NOT NULL,
                description VARCHAR(100) NOT NULL
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS orders (
                orderId SERIAL PRIMARY KEY,
                customerId SERIAL PRIMARY KEY,
                quantity VARCHAR(50) NOT NULL,
                status VARCHAR(50) NOT NULL UNIQUE,
                today VARCHAR(100) NOT NULL
            )
            """
        )
        for query in queries:
            self.cursor.execute(query)


    def delete_tables(self):
        '''This function deletes the tables after usage'''
        delete_queries = (
            """
            DROP TABLE IF EXISTS customers CASCADE
            """,

            """
            DROP TABLE IF EXISTS meals CASCADE
            """,

            """
            DROP TABLE IF EXISTS orders CASCADE
            """
        )
        for query in delete_queries:
            self.cursor.execute(query)
