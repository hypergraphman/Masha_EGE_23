from itertools import product

words = product('АКЛОШ', repeat=5)
for i, w in enumerate(words, start=1):
    word = ''.join(w)
    if word == 'ШКОЛА':
        print(i)

alf = 'АКЛОШ'
k = 1
for c1 in alf:
    for c2 in alf:
        for c3 in alf:
            for c4 in alf:
                for c5 in alf:
                    if c1 + c2 + c3 + c4 + c5 == 'ШКОЛА':
                        print(k, c1 + c2 + c3 + c4 + c5)
                    k += 1
