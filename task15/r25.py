for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        A = x & 125 != 1
        B = x & 34 == 2
        C = x & a == 0
        if not (A or (B <= C)):
            is_a = False
            break
    if is_a:
        print(a)
        break
