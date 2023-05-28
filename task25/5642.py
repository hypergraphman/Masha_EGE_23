def f(n):
    divs = {1, n}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(divs)


from re import fullmatch
i = 500000
c = 0
while c < 5:
    d = f(i)
    k = 0
    for t in d:
        if fullmatch(r'\d*1\d3', str(t)):
            k += 1
    if k == 3:
        print(i, d[-2])
        c += 1
    i += 1