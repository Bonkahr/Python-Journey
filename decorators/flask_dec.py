from flask import Flask

app = Flask(__name__)


@app.route('/')
def print_heading():
    return '<h1>Here we are with Flask</h1>'


@app.route('/fib')
def list_fib():
    return '<b>1, 1, 2, 3, 5, 8, 13, 21 .....</b>'
