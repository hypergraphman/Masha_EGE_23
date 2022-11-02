n = int(input())
prev = 1
cur = 1
i = 2
while i < n:
    prev, cur = cur, cur + prev
    i += 1
print(cur)