def f(a, b, c, m):
    if a + b >= 73:
        return c % 2 == m % 2
    if c == m:
        return 0
    moves = [f(a + 2, b, c + 1, m), f(a, b + 2, c + 1, m), f(a * 2, b, c + 1, m), f(a, b * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)  # any, если первый ход пети был неудачный


# for b in range(1, 63):
#     for m in range(1, 5):
#         if f(9, b, 0, m) == 1:
#             print(b, m)

for h2 in range(1, 63):
    if f(9, h2, 0, 4):
        print(h2)