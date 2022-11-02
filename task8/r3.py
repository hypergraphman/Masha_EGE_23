from itertools import product

alf = 'КЛРТ'
for i, w in enumerate(product(alf, repeat=4), start=1):
    if i == 67:
        print(w)