with open('26-75.txt') as f:
    n = int(f.readline())
    a = []
    for line in f.readlines():
        t1, t2 = line.split()
        t1 = int(t1)
        t2 = -int(t2)
        a.append(t1)
        a.append(t2)
    a.sort(key=lambda x:abs(x))

# print(a)

k = 0
max_k = 0
s = 0
first = None
for t in a:
    if t > 0:
        if not first:
            first = t
        k += 1
        max_k = max(max_k, k)
    else:
        k -= 1
        if k == 0:
            s += abs(t) - first
            first = None
print(max_k, s)
