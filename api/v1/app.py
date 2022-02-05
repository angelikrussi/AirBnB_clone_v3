#!/usr/bin/python
""" app.py """
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
""" Close Storage """

@app.teardown_appcontext
def close_base(self):
    """ Close base data """
    storage.close()



if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))