a = [int(x) for x in open('17-243.txt').readlines()]
sum_digit_mod_35 = 0
for num in a:
    if num % 35 == 0:
        while num > 0:
            sum_digit_mod_35 += num % 3
            num //= 3


def check(p1, p2):
    return p1 > sum_digit_mod_35 >= p2 and p2 % 16 ** 2 == 14 * 16 + 15


count = 0
mn = 10**16
for i in range(1, len(a)):
    x1, x2 = a[i - 1], a[i]
    if check(x1, x2) or check(x2, x1):
        count += 1
        mn = min(x1 + x2, mn)
print(count, mn)

