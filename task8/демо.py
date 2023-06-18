print(3 * 7 ** 3 + 2 * 3 * 7 * 7 + 6 * 3 * 3 * 7 * 2 + 6 * 7 * 7 * 3)


from itertools import product

numbers = product('01234567', repeat=5)
s = set()
for n in numbers:
    num = ''.join(n)
    if (num[0] != '0' and num.count('6') == 1 and
       '16' not in num and '61' not in num and
       '36' not in num and '63' not in num and
       '56' not in num and '65' not in num and
       '76' not in num and '67' not in num):
        s.add(num)
print(len(s))