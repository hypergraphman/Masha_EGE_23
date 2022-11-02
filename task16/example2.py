from functools import cache


@cache
def fib(x):
    if x == 1 or x == 2:
        return 1
    if x > 2:
        return fib(x - 1) + fib(x - 2)


print(fib(int(input())))
