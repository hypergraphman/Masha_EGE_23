with open("26_.txt") as Fin:
    data = Fin.readlines()
n = int(data[0])

kol = 0
skidka = 0
del data[0]
data = sorted( list(map(int, data)) )
s = data[0] + data[1]
for i in range(2, n):
    s += data[i]
    if data[i] == data[i-1] and data[i] == data[i-2]:
        skidka += data[i]
        kol += 1
        data[i] = 0
print(s - skidka, kol)