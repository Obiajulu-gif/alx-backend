#!/usr/bin/env python3
"""
A Flask app enhanced with Flask-Babel for i18n,
with parametrized locale selection
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from config import Config  # Assuming Config is defined elsewhere

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Select a language translation for the user based on the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index.html template with localized text.
    """
    return render_template(
        '3-index.html',
        home_title=_("Welcome to Holberton"),
        home_header=_("Hello world!"))


if __name__ == '__main__':
    app.run(debug=True)
