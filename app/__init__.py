from flask import Flask
from flask_jwt_extended import JWTManager
import datetime
from flask import jsonify

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'my-secret'
app.config['JWT_ACCESS_TOKEN EXPIRES'] = datetime.timedelta(days=2)
jwt = JWTManager(app)

@app.errorhandler(404)
def page_not_found(e):
    """catch the error incase of invalid url"""
    response = jsonify({"message": "A valid URL is required"})
    response.status_code = 404
    return response

from app.views import views, order_views, menu_views
