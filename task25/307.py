from itertools import product
from re import fullmatch


def divs(n):
    d = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


*nums, = product('0123456789', repeat=3)
for i in nums:
    i = ''.join(i)
    if '4' in i and '8' in i:
        num = '12' + i
        d = divs(int(num))
        if len(d) == 4:
            t = d[1] + d[2]
            if len(divs(t)) == 2 and fullmatch(r'12\d*4\d*8\d', num):
                print(num, t)

# 124282 62143
# 1204282 602143
# 1214182 607093
# 1224082 612043
# 1229482 614743
# 1244482 622243
# 1295482 647743