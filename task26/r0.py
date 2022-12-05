f = open('26.txt')
s, n = map(int, f.readline().split())
data = sorted(map(int, f.readlines()))
# print(s, n)
# print(data)
k = 0
while s - data[k] >= 0:
    s -= data[k]
    k += 1
print(k)
mx_v = data[k - 1]
s += data[k - 1]
while s - data[k] >= 0:
    mx_v = data[k]
    k += 1
print(data[k - 1])
