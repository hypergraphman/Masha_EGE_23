from itertools import product, permutations

v1 = []
v2 = []

alf1 = 'mari'
alf2 = 'ina'

for word in permutations(alf1):
    word = ''.join(word)
    v1.append(word)

for word in product(alf2, repeat=4):
    word = ''.join(word)
    v2.append(word)

all_ = set()
for word1 in v1:
    for word2 in v2:
        all_.add(word1 + word2)

for num, word in enumerate(sorted(all_), start=1):
    if word == 'marianna':
        print(num)