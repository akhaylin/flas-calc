import operations
from flask import Flask, request

app = Flask(__name__)

all_ops = {
    "add" : operations.add,
    "sub" : operations.sub,
    "mult" : operations.mult,
    "div" : operations.div
}

#TODO: add docstrings

@app.get('/add')
def add():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return str(operations.add(a,b))


@app.get('/sub')
def sub():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return str(operations.sub(a,b))


@app.get('/mult')
def mult():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return str(operations.mult(a,b))


@app.get('/div')
def div():
    a = float(request.args["a"])
    b = float(request.args["b"])
    return str(operations.div(a,b))


@app.get('/math/<operation>')
def do_calculations(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{all_ops.get(operation)(a,b)}"