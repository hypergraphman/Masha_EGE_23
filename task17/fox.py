*a, = map(int, open('17.txt'))

k = 0
for el in a:
    if abs(el) % 10 == 5:
    # if str(el)[-1] == '5':
        k += 1

res = []
for p1, p2 in zip(a, a[1:]):
    if (((p1 >= 0 and p2 < 0) or (p1 < 0 and p2 >= 0)) and
       p1 + p2 <= k):
        res.append(p1 + p2)
print(len(res), max(res))