def divs(d):
    r = {1, d}
    for i in range(2, int(d ** 0.5) + 1):
        if d % i == 0:
            r.add(i)
            r.add(d // i)
    return sorted(r)


for n in range(0, 10):
    if len(divs(117 + 4 * n)) == 2:
        print(n)