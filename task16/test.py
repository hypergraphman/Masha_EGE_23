cur, nxt = 1, 1
for i in range(2, 57 + 1):
    cur, nxt = nxt, cur + nxt + 1
print(cur)


from functools import cache


@cache
def f(n):
    if n <= 2:
        return 1
    return f(n - 1) + f(n - 2) + 1


print(f(57))
