from app import app
from app.database.dbmanager import DatabaseConnection


if __name__== "__main__":
    DatabaseConnection().create_tables()
    app.run(debug=True)
