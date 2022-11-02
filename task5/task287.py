def f(n):
    d = bin(n)[2:]
    if n % 2 == 0:
        return int('1' + d + '11', 2)
    return int('11' + d + '0', 2)


print(f(100))
c = 0
for i in range(1, 1000):
    if 500 <= f(i) <= 1000:
        print(i)
        c += 1
print(c)