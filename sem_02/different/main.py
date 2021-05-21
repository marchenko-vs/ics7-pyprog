from math import *

def f(x):
    return x * x * x + x * x - 1

def g(x):
    return 1 / sqrt(1 + x)

def steffensen_method(left_b, eps=1e-3, max_iter=500):
    x = left_b
    i = 0
    while abs(f(x)) > eps and i < max_iter:
        i += 1
        x = x - ((f(x) * f(x)) / (f(x + f(x)) - f(x)))
    if abs(f(x)) <= eps:
        return x
    else:
        print('Not Convergent!')
        return


def bisection_metod(x0, x1, eps=1e-3, max_iter=500):
    i = 0
    condition = True
    while condition and i < max_iter:
        x = (x0 + x1) / 2
        if f(x0) * f(x) < 0:
            x1 = x
        else:
            x0 = x
        i += 1
        condition = abs(f(x)) > eps
    return x

def fixed_point_iteration(x0, e, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

