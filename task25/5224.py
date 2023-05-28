from re import fullmatch

for i in range(1, 10**5):
    q = i * i
    if fullmatch(r'4\d*1\d009', str(q)):
        print(i, q)