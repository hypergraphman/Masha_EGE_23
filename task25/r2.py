def dels(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


for i in range(174457, 174505 + 1):
    d = dels(i)
    if len(d) == 4:
        print(d[1], d[2], d[1] * d[2])