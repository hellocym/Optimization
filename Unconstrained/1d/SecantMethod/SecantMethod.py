import numpy as np


def SecantMethod(f, g, xm1, x0, stop_criteria, eps=None, N=None):
    '''
    g: gradient of f
    Use Secant Method to find the minimum of f, or find x s.t. g=0
    In Newton's method, x ← x - f'/f"
    Secant method approximates f" with f'
    f" = (f'(x_k) - f'(x_{k-1})) / (x_k - x_{k-1})
    Thus x_{k+1} = x_k - (x_k - x_{k-1}) / (f'(x_k) - f'(x_{k-1})) * f'(x_k)
    or x_{k+1} = (f'(x_k) * x_{k-1} - f'(x_{k-1}) * x_k) / (f'(x_k) - f'(x_{k-1}))
    Stop criteria: |x_{k+1} - x_k| < eps
    '''
    if stop_criteria not in ['eps', 'maxiter', 'epsx']:
        raise NotImplementedError
    x_pre = xm1
    x = x0
    print(f'x_0={x}, x_-1={x_pre}')
    i = 1
    while True:
        x, x_pre = (g(x) * x_pre - g(x_pre) * x) / (g(x) - g(x_pre)), x
        print(f'x{i}={x}, x_{i-1}={x_pre}')
        i += 1
        if stop_criteria == 'eps':
            if abs(x - x_pre) < eps:
                break
        elif stop_criteria == 'maxiter':
            if i > N:
                break
        elif stop_criteria == 'epsx':
            if abs(x - x_pre) < abs(x_pre) * eps:
                break


def SecantMethodSolve(g, xm1, x0, stop_criteria, eps=None, N=None):
    '''
    Use Secant Method to solve g(x)=0
    Stop criteria: |x_{k+1} - x_k| < eps
    '''
    if stop_criteria not in ['eps', 'maxiter', 'epsx']:
        raise NotImplementedError
    x_pre = xm1
    x = x0
    print(f'x_-1={x_pre}, x_0={x}')
    i = 1
    while True:
        # print((g(x_pre) * x_prepre - g(x_prepre) * x_pre) / (g(x_pre) - g(x_prepre)))
        # return
        x, x_pre = (g(x) * x_pre - g(x_pre) * x) / (g(x) - g(x_pre)), x
        print(f'x{i}={x}')
        i += 1
        if stop_criteria == 'eps':
            if abs(x - x_pre) < eps:
                break
        elif stop_criteria == 'maxiter':
            if i > N:
                break
        elif stop_criteria == 'epsx':
            if abs(x - x_pre) < abs(x_pre) * eps:
                break
    print(f'g({x:.4f}) = {g(x):.4f}')



if __name__ == '__main__':
    # g = lambda x: x**3 - 12.2*x**2 + 7.45*x + 42
    # SecantMethodSolve(g, xm1=13, x0=12, stop_criteria='maxiter', N=2)

    g = lambda x: (2*x-1)**2 + 4*(4-1024*x)**4
    SecantMethodSolve(g, xm1=0, x0=1, stop_criteria='epsx', eps=1e-5)

