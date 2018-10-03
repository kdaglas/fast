import psycopg2
# from app import app
import psycopg2.extras as naome


class DatabaseConnection:

    def __init__(self):
        '''This constructor creates a connection to the database'''
        # if app.config['TESTING']:
        #     print("Testing")
        #     self.con = psycopg2.connect(database="testdb", user="postgres",
        #                                 password="admin", host="localhost",
        #                                 port="5432"
        #                                 )
        # else:
        #     print("Development")
        #     self.con = psycopg2.connect(database="postgres", user="postgres",
        #                                 password="admin", host="localhost",
        #                                 port="5432"
        #                                 )
        
        self.con = psycopg2.connect(database="postgres", user="postgres",
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
                contact VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(25) NOT NULL
            );
            """,

            """
            CREATE TABLE IF NOT EXISTS meals (
                mealId SERIAL PRIMARY KEY,
                thetype VARCHAR NOT NULL,
                food VARCHAR NOT NULL UNIQUE,
                price INTEGER NOT NULL,
                description VARCHAR(100) NOT NULL
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS orders (
                orderId SERIAL PRIMARY KEY,
                customerId INTEGER,
                mealId INTEGER,
                quantity INTEGER NOT NULL,
                status VARCHAR(50),
                today VARCHAR(100) NOT NULL,
                FOREIGN KEY (customerId) REFERENCES customers(customerId) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (mealId) REFERENCES meals(mealId) ON UPDATE CASCADE ON DELETE CASCADE
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


# DB = DatabaseConnection()
# DB.create_tables()