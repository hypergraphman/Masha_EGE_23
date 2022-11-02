import re

data = open('24-230.txt').readline().split('KK')

nums = []
for line in data:
    if re.search(r'43\d\d78\d\d\d34', line):
        nums.append(int(re.search(r'43\d\d78\d\d\d34', line)[0]))
num = str(max(nums))
p = 1
for el in map(int, num):
    if el % 2:
        p *= el
print(p)