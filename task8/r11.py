from itertools import product
alf = 'школа'
c = 0
for word in product(alf, repeat=3):
    w = ''.join(word)
    if word.count('к') == 1:
        c += 1
print(c)