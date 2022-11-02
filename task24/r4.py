line = open('k7.txt').readline()
c = 0
for i in range(2, len(line)):
    s1, s2, s3 = line[i - 2], line[i - 1], line[i]
    if (s1 in 'BCD' and s2 in 'BDE' and s2 != s1 and
       s3 in 'BCE' and s3 != s2):
        c += 1
print(c)
