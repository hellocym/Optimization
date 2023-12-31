import numpy as np


def GoldenSectionSearch(f, a0, b0, N):
    '''
    N: Max-Iteration

    Only for unimodal function
    Choose a1, b1, where a1 - a0 = b0 - b1 = ρ(b0 - a0), ρ = (3-√5)/2 ≈ 0.382
    If f(a1) < f(b1), then GoldenSectionSearch(f, a0, b1);
    Else GoldenSectionSearch(f, a1, b0)
    '''
    ρ = (3 - 5 ** 0.5) / 2
    am = a0 + ρ * (b0 - a0)
    bm = a0 + (1 - ρ) * (b0 - a0)
    for i in range(1, N+1):
        print(f'Iter {i}: GoldenSectionSearch in [{a0}, {b0}]')
        print(f'f(am) = {f(am)}, f(bm) = {f(bm)}')
        if f(am) < f(bm):
            a0, b0 = a0, bm
            am, bm = a0 + ρ * (bm - a0), am
        else:
            a0, b0 = am, b0
            am, bm = bm, b0 - ρ * (b0 - am)
        print(f'Minimum is in [{a0}, {b0}]')

if __name__ == '__main__':
    f = lambda x: x**4 - 14*x**3 + 60*x**2 - 70*x
    GoldenSectionSearch(f, 0, 2, 4)
    
