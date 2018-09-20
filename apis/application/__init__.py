from flask import Flask

webapp = Flask(__name__)

from apis.application import routes
