#!/usr/bin/python3
"""
This is module 9-states.

In this module, we combine Flask with SQLAlchemy for the first time.
Run this script from the AirBnB_v2 directory for imports.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states/')
@app.route('/states/<id_d>')
def cities_by_states(id_d="all"):
    """
    Display a web page with a list of states or cities in a specific state.

    Parameters:
        id_d (str): State ID or 'all' to display all states.

    Returns:
        str: Rendered HTML template.
    """
    states = storage.all("State")
    if id_d == "all":
        return render_template("9-states.html", state="all",
                               Query_name="States",
                               states=states.values())
    else:
        flag = False
        for k, v in states.items():
            if k == id_d:
                flag = True
                break
        if flag:
            result = v.cities
            return render_template("9-states.html", state="1",
                                   Query_name="State: {}".format(v.name),
                                   states=result)
        else:
            return render_template("9-states.html", state="",
                                   Query_name="Not found!",
                                   states=states)


@app.teardown_appcontext
def close_session(exception):
    """Remove the db session or save file."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

