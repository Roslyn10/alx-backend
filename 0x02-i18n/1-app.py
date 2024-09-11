#!/usr/bin/env python3
"""A simple flask setup using babel"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configures available languages in the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def index():
    """
    The index page to be displayed on the website.

    This function renders the index template which uses translated 
    strings based on the selected locale.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
