import numpy as np
from math import sin, cos


def NewtonsMethod(f, g, h, eps, x0):
    '''
    g: gradient of f
    h: hessian of f
    Use Newton's Method to find the minimum of f, or find x s.t. g=0
    x ← x - f'/f"
    or x ← x - g/g' 
    or x ← x - g/h
    Stop criteria: |x_{k+1} - x_k| < eps
    '''
    i = 0
    x = x_last = x0
    while True:
        print(f'x{i} = {x}')
        x -= g(x) / h(x)
        i += 1
        if abs(x - x_last) < eps:
            break
        x_last = x
    print(f'x{i} = {x}')
    

def NewtonsMethodSolve(g, h, eps, x0):
    '''
    h: hessian of g
    Use Newton's Method to solve g(x)=0

    x ← x - g/g' 
    or x ← x - g/h
    Stop criteria: |x_{k+1} - x_k| < eps
    '''
    i = 0
    x = x_last = x0
    while True:
        print(f'x{i} = {x}')
        x -= g(x) / h(x)
        i += 1
        if abs(x - x_last) < eps:
            break
        x_last = x
    print(f'x{i} = {x}')


if __name__ == '__main__':
    f = lambda x: 1/2*x**2 - sin(x)
    g = lambda x: x - cos(x)
    h = lambda x: 1 + sin(x)
    NewtonsMethod(f, g, h, eps=1e-5, x0=0.5)
    
    g = lambda x: x**3 - 12.2*x**2 + 7.45*x + 42
    h = lambda x: 3*x**2 - 24.4*x + 7.45
    NewtonsMethodSolve(g, h, eps=1e-5, x0=12)
