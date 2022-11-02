for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        A = x % a != 0
        B = x % 6 == 0
        C = x % 9 != 0
        if not (A <= (B <= C)):
            is_a = False
            break
    if is_a:
        print(a)

print('----------------')
for a in range(1, 1000):
    if all((x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0)) for x in range(1, 1000)):
        print(a)