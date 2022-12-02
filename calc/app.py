from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def flask_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result =  add(a, b)
    return str(result)

@app.route('/sub')
def flask_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result =  sub(a, b)
    return str(result)

@app.route('/mult')
def flask_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result =  mult(a, b)
    return str(result)

@app.route('/div')
def flask_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result =  div(a, b)
    return str(result)

MATH = {
    'add': add,
    'sub': sub,
    'mult':mult,
    'div': div,
}

@app.route('/math/<operation>')
def do_math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result =  MATH[operation](a, b)

    return str(result)
