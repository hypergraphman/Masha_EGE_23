from itertools import product

words = product('AYKLE', repeat=5)
for i, w in enumerate(words, start=1):
    word = ''.join(w)
    if word.count('K') <= 1 and 'EE' not in word:
        print(i, w)