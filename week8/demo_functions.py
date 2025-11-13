def add(a, b):
    c = a + b
    return c

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Không chia được cho 0")
    c = a / b
    return c

def sum(n):
    if n < 0:
        raise ValueError("n must >= 0")
    s = 0
    for i in range(1, n+1):
        s += i
    return s