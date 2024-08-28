#!/usr/bin/env python3
"""
A Flask app enhanced with Flask-Babel for i18n,
with parametrized locale selection
"""
from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel()

babel.init_app(app)


@app.route('/')
def index():
    """
    Render the index.html template
    """
    return render_template(
        '3-index.html',
        home_title=_("Welcome to Holberton"),
        home_header=_("Hello world!"))


if __name__ == '__main__':
    app.run(debug=True)
