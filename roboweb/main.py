from flask import Flask, Response, request
from func.service import Arm
import time
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<center> <br> <h1>Hello, World!</p>"


@app.route('/index')
def index():
    return "<center> <br> <h2>This is the index page</h2>"


@app.route('/move')
def move():
    def inner():
        yield "....Moving x-axis to the right"
        # Arm.move_x_axis()
        yield "<br>....Movement done"
    return Response(inner())
