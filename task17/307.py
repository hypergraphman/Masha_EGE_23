with open('17-304.txt') as f:
    a = list(map(int, f.readlines()))

min_odd = 10**10
for el in a:
    if el % 2 != 0 and el < min_odd:
        min_odd = el
r = []
for x, y in zip(a, a[1:]):
    if (x + y) % min_odd == 0:
        sum_x_even = sum(filter(lambda i: i % 2 == 0, map(int, str(x))))
        sum_x_odd = sum(filter(lambda i: i % 2 != 0, map(int, str(x))))
        sum_y_even = sum(filter(lambda i: i % 2 == 0, map(int, str(y))))
        sum_y_odd = sum(filter(lambda i: i % 2 != 0, map(int, str(y))))
        if sum_x_even < sum_x_odd and sum_y_even < sum_y_odd:
            r.append(x + y)
print(len(r), min(r))