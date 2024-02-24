#!/usr/bin/python3
"""
This is module 6-number_odd_or_even.

It starts a minimal Flask application.
Run it with python3 -m 6-number_odd_or_even or ./6-number_odd_or_even
"""
from flask import Flask, render_template

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


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<text>')
def python_text(text):
    """Give a rule a default value."""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number_route(n):
    """Make a rule only take a number."""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:number>')
def number_template(number):
    """Create an HTML page with a rule."""
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Create a template with 2 variables."""
    odd_even = "even" if (n % 2 == 0) else "odd"
    return render_template("6-number_odd_or_even.html",
                           number=n, odd_even=odd_even)

if __name__ == "__main__":
    # Values here are the default, mentioned as keepsake.
    app.run(host="0.0.0.0", port="5000")
