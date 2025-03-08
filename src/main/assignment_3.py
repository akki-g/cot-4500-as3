

def eulersMethod(f, a, b, n, y0):
    h = (b-a)/n 
    t = a
    w = y0

    for _ in range(n):
        w = w + h*f(t, w)
        t = t + h

    return w


def rungeKutta(f, a, b, n, y0):
    h = (b-a)/n
    t = a
    w = y0

    for _ in range(n):
        k1 = h*f(t, w)
        k2 = h*f(t + h/2, w + k1/2)
        k3 = h*f(t + h/2, w + k2/2)
        k4 = h*f(t + h, w + k3)
        w = w + (k1 + 2*k2 + 2*k3 + k4)/6
        t = t + h

    return w





