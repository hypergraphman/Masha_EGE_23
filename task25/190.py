from functools import lru_cache

@lru_cache(None)
def dels(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


@lru_cache(None)
def s(n):
    t = dels(n)
    if len(t) < 3:
        return 0
    return sum(t[-3:])


x = 10_000_000
k = 5
while k:
    if s(x) and s(x)**0.5 == int(s(x)**0.5):
        k -= 1
        print(s(x))
    x += 1