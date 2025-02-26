#!/usr/bin/python3
"""
A script that starts a Flask web application:
"""

from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_route():
    """
    Displays 'Hello HBNB!'
    Returns:
        str: "Hello HBNB"
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
