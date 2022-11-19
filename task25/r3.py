def dels(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


# print(dels(1))
primes = []
for i in range(3, 100):
    if len(dels(i)) == 2:
        primes.append(i)

# print(primes)
ans = []
for x in range(27):
    for p in primes:
        t = 2**x * p**4
        if 77_777_777 <= t <= 88_888_888:
            ans.append((t, p))
ans.sort()
for n, p in ans:
    print(n, p)