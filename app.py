from flask_injector import FlaskInjector
from flask import Flask, Config
from flask.views import View
from injector import inject
from webLlib.ResponseProcessor import ResponseProcessor
from routes import routesBluePrint
import pprint

printer = pprint.PrettyPrinter(indent=4)
responseProcessor = ResponseProcessor(debug=True)
app = Flask('Pick2Story')

app.register_blueprint(routesBluePrint)


if __name__ == '__main__':
    printer.pprint(app.url_map)
    app.run('localhost', 9000)

