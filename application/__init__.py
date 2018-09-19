from flask import Flask

webapp = Flask(__name__)

from application import routes
