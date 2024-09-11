#!/usr/bin/env python3
"""A Simple flask setup"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """
    The index page to be displayed on the website.

    This function renders the index template which uses translated
    strings based on the selected locale.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
