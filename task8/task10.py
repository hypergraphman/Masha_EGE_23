from itertools import product

alf = 'aoy'

for num, word in enumerate(product(alf, repeat=5), start=1):
    if ''.join(word) == 'oaoao':
        print(num)