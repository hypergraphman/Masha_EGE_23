with open('76test.txt') as f:
    dl, n = map(int, f.readline().split())
    a = []
    for l in f.readlines():
        t1, t2 = l.split()
        t1 = int(t1)
        t2 = -int(t2)
        a.append(t1)
        a.append(t2)
a.sort(key=lambda x: abs(x))
print(a)
max_pr = 0
pr = 0
k = 0
s = 0
first = 0
for t in a:
    if t >= 0:
        k += 1
        if k == 1:
            pr = t - first
            max_pr = max(pr, max_pr)
            s += pr
    else:
        k -= 1
        if k == 0:
            first = -t
pr = dl - first
max_pr = max(pr, max_pr)
s += pr
print(s, max_pr)