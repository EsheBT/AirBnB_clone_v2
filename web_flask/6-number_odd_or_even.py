#!/usr/bin/python3
"""
A script that starts a Flask web application:
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Displays 'Hello HBNB!'
    Returns:
        str: "Hello HBNB"
    """
    return "Hello HBNB!"


