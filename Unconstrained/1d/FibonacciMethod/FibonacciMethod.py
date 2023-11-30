import numpy as np


def F(i: int):
    '''
    Fibonacci Sequence
    '''
    if i == 0 or i == 1:
        return 1
    else:
        return F(i - 1) + F(i - 2)

def FibonacciMethod(f, a0, b0, N, eps=0.05):
    '''
    N: Max-Iteration

    For Iteration k, Choose a1, b1, where a1 - a0 = b0 - b1 = ρk(b0 - a0), ρk = 1 - F_{N-k+1}/F{N-k+2}
    If f(a1) < f(b1), then FibonacciMethod(f, a0, b1);
    Else FibonacciMethod(f, a1, b0)
    Final iteraton: ρN = 1/2 - eps
    '''
    
    # return
    ρ = 1 - F(N) / F(N+1)
    am = a0 + ρ * (b0 - a0)
    bm = a0 + (1 - ρ) * (b0 - a0)
    for i in range(1, N+1):
        print(f'Iter {i}: FibonacciMethod in [{a0}, {b0}]')
        print(f'ρ{i} = {ρ}')
        print(f'f(am) = {f(am)}, f(bm) = {f(bm)}')
        ρ = 1 - F(N-i) / F(N-i+1)
        if i == N-1:
            ρ -= eps
        if f(am) < f(bm):
            a0, b0 = a0, bm
            am, bm = a0 + ρ * (bm - a0), am
        else:
            a0, b0 = am, b0
            am, bm = bm, b0 - ρ * (b0 - am)
        print(f'Minimum is in [{a0}, {b0}]')
        

if __name__ == '__main__':
    f = lambda x: x**4 - 14*x**3 + 60*x**2 - 70*x
    FibonacciMethod(f, 0, 2, 4)
    # print([F(i) for i in range(10)])
    
