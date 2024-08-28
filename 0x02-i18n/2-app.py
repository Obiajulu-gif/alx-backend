#!/usr/bin/env python3
"""
A Flask app enhanced with Flask-Babel for i18n,
with locale selection based on request
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
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
    Render the index.html template
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
