import re

data = open('24-230.txt').readline().split('ZZ')

nums = []
for line in data:
    if re.fullmatch(r'8\d\d\d54\d\d\d22', line):
        print(line)
        nums.append(int(re.fullmatch(r'8\d\d\d54\d\d\d22', line)[0]))
num = str(max(nums))
p = 1
for el in map(int, num):
    if el % 2:
        p *= el
print(p)