line = open('24.txt').readline()
mx_len = 1
cur_len = 1
for i in range(1, len(line)):
    s1, s2 = line[i - 1], line[i]
    if s1 != s2:
        cur_len += 1
        if mx_len < cur_len:
            mx_len = cur_len
    else:
        cur_len = 1
print(mx_len)