f = open('26-j2.txt')
n = int(f.readline())
a = sorted(map(int, f.readlines()))
avg = sum(a)/len(a)
m = a[len(a)//2]
k = 0
print(avg, m)
for el in a:
    if avg <= el <= m:
        k += 1
print(k)