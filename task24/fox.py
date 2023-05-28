s = open('24.txt').read()
cur_len = 0
max_len = 0
for i in range(2, len(s), 3):
    if s[i: i + 3] in ('FEG', 'GEF'):
        cur_len += 1
        max_len = max(cur_len, max_len)
    else:
        cur_len = 0
print(max_len) # 16