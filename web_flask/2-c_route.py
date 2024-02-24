#!/usr/bin/python3
"""
This is module 2-c_route.

It starts a minimal Flask application.
Run it with python3 -m 2-c_route or ./2-c_route
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    """Flask hello world."""
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """Add a path to the URL."""
    return "HBNB"

@app.route('/c/<text>')
def c_text(text):
    """Make a simple variable rule."""
    return "C {}".format(text.replace("_", " "))

if __name__ == "__main__":
    # Values here are the default, mentioned as keepsake.
    app.run(host="0.0.0.0", port="5000")
