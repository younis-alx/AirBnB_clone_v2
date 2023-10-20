#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """return hello hbnb!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return hbnb!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cSomething(text):
    """display C with variable """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pySomething(text='is_cool'):
    """display C with variable """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display n is a number only if n is an integer"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
