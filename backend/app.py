"""Main Flask entry point."""

from flask import Flask
from flask_cors import CORS
import logging

LOG = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# @app.route('/<name>')
# def hello(name):
#     """Hello world."""
#     return f'Hello {name}!'

@app.route('/greeting')
def greeting():
    """Greeting."""
    return {"greeting": "Hello from the backend!"}

@app.route('/')
def hello_world():
    LOG.error('Hello World from logging!')
    return {"greeting": "Hello from the main!"}