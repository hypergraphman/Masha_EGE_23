for i in range(-1000, 1000):
    s = i
    n = 0
    while s <= 275:
        s = s + 5
        n = n + 2
    if n < 195:
        print(i)