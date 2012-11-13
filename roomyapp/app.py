from flask import Flask
from api import ApiView
from logbook import Logger

app = Flask(__name__)
log = Logger(__name__)

ApiView.register(app, route_base='/')

if __name__ == "__main__":
    app.run(debug=True)
