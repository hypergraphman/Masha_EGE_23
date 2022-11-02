def f(n):
    if n < 2:
        return n
    if n >= 2 and n % 2 == 0:
        return f(n // 2) + 1
    return f(3 * n) + 1


amount = 0
for i in range(1, 100 + 1):
    try:
        if f(i) != 0:
            amount += 1
    except:
        print(f'f({i}) - не сработала')
print(amount)