import psycopg2
from app import app
import psycopg2.extras as dictionary


class DatabaseConnection:

    def __init__(self):

        '''This constructor creates a connection to the database depending on the configuration
            meaning if its a test data, then a test database is used where as if its a development
            data then a development database is created'''
        try:
            if not app.config['TESTING']:
                self.con = psycopg2.connect(database="fastfoodfastdb", user="postgres",
                                            password="admin", host="localhost",
                                            port="5432"
                                            )
            else:
                self.con = psycopg2.connect(database="testdb", user="postgres",
                                            password="admin", host="localhost",
                                            port="5432"
                                            )
            self.con.autocommit = True
            self.cursor = self.con.cursor(cursor_factory = dictionary.RealDictCursor)
        except Exception as e:
            print(e)
            print('Cannot connect to the database')

    
    def create_tables(self):
        '''This function creates the tables'''
        queries = (
            """
            CREATE TABLE IF NOT EXISTS admin (
                adminId SERIAL PRIMARY KEY NOT NULL,
                username VARCHAR NOT NULL,
                password VARCHAR NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS customers (
                customerId SERIAL PRIMARY KEY NOT NULL,
                username VARCHAR NOT NULL,
                contact VARCHAR NOT NULL,
                password VARCHAR NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS menu (
                mealId SERIAL PRIMARY KEY NOT NULL,
                thetype VARCHAR NOT NULL,
                food VARCHAR NOT NULL,
                price INTEGER NOT NULL,
                description VARCHAR NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS orders (
                orderId SERIAL PRIMARY KEY NOT NULL,
                customerId INTEGER NOT NULL,
                mealId INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                status VARCHAR NOT NULL,
                today TEXT NOT NULL DEFAULT TO_CHAR(CURRENT_TIMESTAMP, 'YYYY-MM-DD'),
                FOREIGN KEY (customerId) REFERENCES customers(customerId) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (mealId) REFERENCES menu(mealId) ON DELETE CASCADE ON UPDATE CASCADE
            )
            """
        )
        for query in queries:
            self.cursor.execute(query)


    def delete_tables(self):
        '''This function deletes the tables after usage'''
        delete_queries = (
            """DROP TABLE IF EXISTS customers CASCADE""",
            """DROP TABLE IF EXISTS menu CASCADE""",
            """DROP TABLE IF EXISTS orders CASCADE"""
        )
        for query in delete_queries:
            self.cursor.execute(query)      


    # @staticmethod
    # def update_single_meal(mealId, price):
    #     cursor.execute("UPDATE menu SET price = '{}' WHERE mealId = '{}'".
    #                 format(price, mealId))
    #     rows = cursor.fetchone()
    #     if not rows:
    #         return {"message": "Meal not found"}
    #     return rows  


    def closedb(self):
        """method to close db connection"""
        self.con.close()
