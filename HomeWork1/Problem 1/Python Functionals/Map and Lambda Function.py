# Map and Lambda Function
cube = lambda x: x ** 3

def fibonacci(n):
    a, b, c = 0, 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b