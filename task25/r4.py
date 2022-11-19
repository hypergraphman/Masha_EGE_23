import re
for i in range(2023, 10**10, 2023):
    t = str(i)
    d1 = t[0] == '1'
    d2 = t[1] in '0123456789'
    d2139 = t[2:6] == '2139'
    d_last = t[-1] == '4'
    if d1 and d2 and d2139 and d_last:
    # if re.fullmatch(r'1\d2139\d*4', str(i)):
        print(i, i // 2023)
