def dels(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


def check(x):
    t = dels(x)
    for d1 in t:
        for d2 in t:
            for d3 in t:
                if x / d3 / d2 / d1 == 1:
                    return False
    return True


nk = 19_500_000
k = 1
n = 5
while n:
    if check(nk + k):
        n -= 1
        print(k, dels(nk + k)[-1])
    k += 1