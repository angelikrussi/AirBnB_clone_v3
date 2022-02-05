#!/usr/bin/python3
"""Index"""
from models import storage
from api.v1.views.index import *
from flask import Flask, Blueprint, jsonify


@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """hbnbStatus"""
    return jsonify({"status": "OK"})
