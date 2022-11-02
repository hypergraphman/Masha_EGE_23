from itertools import permutations

alf = 'улей'
c = 0
for w in permutations(alf, r=3):
    word = ''.join(w)
    if word[0] != 'й' and 'еу' not in word:
        print(word)
        c += 1
print(c)
