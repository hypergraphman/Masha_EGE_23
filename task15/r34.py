for a in range(1, 1000):
    is_a = True
    for k in range(1, 1000):
        for n in range(1, 1000):
            B = 5 * k + 6 * n > 57
            C = k <= a
            D = n < a
            if not (B or (C and D)):
                is_a = False
                break
        if not is_a:
            break
    if is_a:
        print(a)
        break