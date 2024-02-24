#!/usr/bin/python3
"""
This is module 7-states_list.i

In this module, we combine Flask with SQLAlchemy for the first time.
Run this script from the AirBnB_v2 directory for imports.
"""
from os import getenv
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list/')
def list_states():
    """List all states in a database."""
    states = storage.all(State).values()
    return render_template("7-states_list.html", Query_name="States", states=states)


@app.teardown_appcontext
def close_session(exception):
    """Remove the session to see what happened."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5300")
