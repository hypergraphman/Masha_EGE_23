def alg(n):
    s1 = f'{n:b}'
    if n % 2:
        s2 = '10' + s1 + '11'
    else:
        s2 = '1' + s1 + '00'
    return int(s2, 2)


a = set()
for i in range(1, 1000):
    r = alg(i)
    if r > 1023:
        a.add(r)
print(min(a))
