a = [0] * 100
a[2] = 1
for i in range(2, 14):
    if i + 1 <= 14:
        a[i + 1] += a[i]
    if i * 2 <= 14:
        a[i * 2] += a[i]
for i in range(14, 29):
    if i + 1 <= 29 and i + 1 != 25:
        a[i + 1] += a[i]
    if i * 2 <= 29 and i * 2 != 25:
        a[i * 2] += a[i]
print(a[29])
print(a[:30])