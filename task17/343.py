def f(n):
    step1 = str(n)[::-1]
    even_sum = sum(map(int, step1[::2]))
    odd_sum = sum(map(int, step1[1::2]))
    if even_sum == 0:
        return False
    return odd_sum % even_sum == 0


a = list(map(int, open('17-343.txt').readlines()))

count = 0
mn = 10**10
for i in range(2, len(a)):
    x1, x2, x3 = a[i - 2], a[i - 1], a[i]
    if f(x1) and f(x2) and f(x3):
        count += 1
        mn = min(mn, x1 + x2 + x3)
print(count, mn)
