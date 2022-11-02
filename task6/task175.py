c = 0
for i in range(1, 10000):
    s = i
    s = s // 5
    n = 8
    while s < 156:
        if (s + n) % 3 == 0:
            s = s + 6
        n = n + 11
    if n == 140:
        print(i)
        c += 1
print(c)