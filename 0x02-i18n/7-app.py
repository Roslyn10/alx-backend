#!/usr/bin/env python3
"""A simple Flask setup using Babel"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from datetime import datetime
import pytz
from pytz import UnknownTimeZoneError


class Config:
    """Configures available languages in the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Returns the user dictionary or None if no ID is found"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Adds a user to the Flask `g`"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match with supported languages.

    This function checks the 'Accept-Language' header from the request
    and matches it with the supported languages defined in the app config.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """A funciton that gets the timezone of the local machine"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    user_timezone = get_user_timezone()
    if user_timezone:
        try:
            pytz.timezone(user_timezone)
            return user_timezone
        except UnknownTimeZoneError:
            pass


@app.route('/')
def index():
    """
    The index page to be displayed on the website.

    This function renders the index template which uses translated
    strings based on the selected locale.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
