s = open('24-181.txt').readline()
words = s.split('.')
# print(s)
# print(words)
lens = []
for word in words:
    lens.append(len(word))
# print(lens)
mx_sum = 0
for p1, p2 in zip(lens, lens[1:]):
    if p1 + p2 > mx_sum:
        mx_sum = p1 + p2
print(mx_sum + 1)