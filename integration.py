from flask import Flask
import math

app = Flask(__name__)

def integration(a, b, N):
    dx = (b-a)/N
    x=a
    sum_left = 0
    sum_right = 0
    for i in range(N):
        sum_left += abs(math.sin(x))*dx
        x+=dx
        sum_right += abs(math.sin(x))*dx
    return sum_left, sum_right

def function_to_integrate(x):
    return abs(math.sin(x))

@app.route('/')
def hello():
    return "<p>Hello !</p>"

@app.route('/<a>/<b>')
def integration_without_N(a, b):
    T=[]
    for N in ([10, 100, 100, 1000, 10000, 100000, 1000000]):
        T+=[(integration(float(a), float(b), N))]
    return T