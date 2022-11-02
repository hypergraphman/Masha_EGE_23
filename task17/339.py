a = list(map(int, open('17-339.txt').readlines()))

search_min = 10**5
for el in a:
    if el % 19 == 0 and el > 0:
        search_min = min(search_min, el)

count = 0
mx = -10**10
for i in range(1, len(a)):
    x1, x2 = a[i - 1], a[i]
    if x1 + x2 < search_min:
        count += 1
        mx = max(mx, x1 + x2)
print(count, abs(mx))
