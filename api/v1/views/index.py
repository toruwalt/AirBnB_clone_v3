#!/usr/bin/python3
"""Index of the app"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route("/status", methods=['GET'], strict_slashes=False)
def return_status():
    return jsonify({"status": "OK"})
