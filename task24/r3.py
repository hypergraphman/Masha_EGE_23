line = open('k7.txt').readline()
mx_len = 0
cur_len = 0
temp = 'EAB'
for s in line:
    if s == temp[cur_len % len(temp)]:
        cur_len += 1
        if mx_len < cur_len:
            mx_len = cur_len
    elif s == 'E':
        cur_len = 1
    else:
        cur_len = 0
print(mx_len)