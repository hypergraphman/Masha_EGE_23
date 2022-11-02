line = open('24.txt').readline()
line = line.replace('D', 'C').replace('F', 'C')
line = line.replace('O', 'A')
line = line.replace('CA', 'O').replace('C', 'A')
print(len(max(line.split('A'))))

mx_len = 0
cur_len = 0
for s in line:
    if s == 'O':
        cur_len += 1
        if mx_len < cur_len:
            mx_len = cur_len
    else:
        cur_len = 0
print(mx_len)