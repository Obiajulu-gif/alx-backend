#!/usr/bin/env python3
"""
a basic Flask app with a single quote
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the index.html template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
