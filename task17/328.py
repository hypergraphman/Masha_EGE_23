def f(x1, x2, x3, avg):
    pair1 = x1 + x2
    pair2 = x1 + x3
    pair3 = x2 + x3
    mn = min(pair1, pair2, pair3)
    return int(pair1**0.5)**2 == pair1 and \
           int(pair2**0.5)**2 == pair2 and \
           int(pair3**0.5)**2 == pair3 and mn > avg


a = list(map(int, open('17-328.txt').readlines()))
s = 0
n = 0
for el in a:
    if el % 50 == 0:
        s += el
        n += 1
avg = s / n

count = 0
mn = 10**10
for i in range(2, len(a)):
    x1, x2, x3 = a[i - 2], a[i - 1], a[i]
    if f(x1, x2, x3, avg):
        count += 1
        mn = min(mn, x1 + x2 + x3)
print(count, mn)
