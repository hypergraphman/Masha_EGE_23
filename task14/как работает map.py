def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def my_map(f, x, y):
    return f(x, y)


print(my_map(add, 4, 6))

s = '234'
print(sum(map(int, s)))
print(sum([int('2'), int('3'), int('4')]))