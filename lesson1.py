from time import time
from sys import setrecursionlimit

def fib_rec(n: int):
    if n in known:
        return known[n]
    result = fib_rec(n - 1) + fib_rec(n - 2)
    known[n] = result
    return result


def fib_linear(index: int):
    if index < 2:
        return index
    count = 1
    first = 0
    second = 1
    while count < index:
        count += 1
        first, second = second, first + second
    return second


def memoize(func):
    cache = {}

    def inner(a):
        nonlocal cache
        return cache.get(a) or cache.setdefault(a, func(a))

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner


@memoize
def fibonacci(n):
    """
    Возвращает n-ое число Фибоначчи
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


known = {1: 1, 2: 1}
ITERATIONS = 10000
setrecursionlimit(100000000)

start = time()
fibonacci(ITERATIONS)
print(f'Рекурсия с декоратором \t\t{time() - start}')

start = time()
fib_rec(ITERATIONS)
print(f'Рекурсия \t\t\t\t\t{time() - start}')

start = time()
fib_linear(ITERATIONS)
print(f'Линейная \t\t\t\t\t{time() - start}')
