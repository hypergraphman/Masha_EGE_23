def f(n):
    s1 = bin(n)[2:]
    if n % 2 == 0:
        s2 = '11' + s1[:-2] + '10'
    else:
        s2 = s1 + '01'
    return int(s2, 2)


print(f(4))  # 30
print(f(5))  # 21

for i in range(1, 20):
    print(i, f(i))