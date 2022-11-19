def dels(n):
    d = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


a = 338472
b = 338494
j = 1
for i in range(a, b + 1):
    t = dels(i)
    if len(t) == 4:
        print(j, *t)
    j += 1
