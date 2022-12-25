f = open('26-j1.txt')
n = int(f.readline())
a = [0] * 100
for _ in range(n):
    t = int(f.readline())
    a[t] += 1
print(a)
k = 0
for i in range(1, 50):
    k += min(a[i], a[100 - i])
k += a[50] // 2
print(k)