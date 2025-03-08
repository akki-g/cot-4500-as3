from src.main.assignment_3 import *


def f(t, y):
    return t - y**2

a, b = 0, 2
n = 10
y0 = 1

result = eulersMethod(f, a, b, n, y0)  

print(result, "\n") 

rkResult = rungeKutta(f, a, b, n, y0)

print(rkResult, "\n")