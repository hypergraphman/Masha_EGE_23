n, *a = map(int, open('26.txt'))
a.sort()
i = 1
k = 0
c = 0
s = a[-1]
while i < len(a):
    if a[-i] == a[-i - 1]:
        k += 1
        if k == 2:
            c += 1
            i += 1
            k = 0
    else:
        k = 0
    s += a[-i]
    i += 1
print(s, c)