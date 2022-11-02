def check(x):
    return bool(list(filter(lambda d: x == d * 197, str(x))))


def f(x1, x2):
    return check(x1) != check(x2)


a = list(map(int, open('17-298.txt').readlines()))

mux = -10 ** 10
for el in a:
    if el % 197 == 0:
        mux = max(mux, el)

count = 0
mx = -10 ** 10
for i in range(1, len(a)):
    x1, x2 = a[i - 1], a[i]
    if x1 + x2 < mux and f(x1, x2):
        count += 1
        mx = max(mx, x1 + x2)
print(count, mx)
