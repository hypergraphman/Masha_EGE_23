def dels(n):
    d = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


a = 394480
b = 394540
# порядковый номер, кол-во делителей, наибольшие делители
max_i = [[2, 2, 1]]
for i in range(a, b + 1):
    t = dels(i)
    if len(t) > max_i[0][0]:
        max_i = [[len(t), i, t[-2]]]
    elif len(t) == max_i[0][0]:
        max_i.append([len(t), i, t[-2]])
j = 1
for mx in max_i:
    print(j, *mx)
    j += 1
