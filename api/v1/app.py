#!/usr/bin/python
""" app.py """
import storage from models
import app_views from api.v1.views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": ["0.0.0.0"]}})


@app.teardown_appcontext
def close_base(self):
    """ Close base data """
    storage.close()


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))
