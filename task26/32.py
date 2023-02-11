from math import ceil

f = open('26-s1.txt')
n = int(f.readline())
a = sorted(map(int, f.readlines()))[::-1]
x = 0
while a[x] <= 150:
    x += 1
do150 = a[:x]
posle150 = a[x:]
skidka = posle150[:len(posle150) // 2]
bez = posle150[len(posle150) // 2:]

print(ceil(sum(skidka) * 0.8) + sum(do150) + sum(bez), skidka[-1])