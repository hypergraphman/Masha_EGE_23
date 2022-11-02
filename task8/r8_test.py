from itertools import product

alf = 'улей'
c = 0
for w in product(alf, repeat=4):
    word = ''.join(w)
    if word[0] != 'й' and 'еу' not in word and len(set(word)) == 4:
        print(word)
        c += 1
print(c)
