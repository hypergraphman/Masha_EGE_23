def f(h1, h2, c, m):
    if h1 + h2 >= 73:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [f(h1 + 2, h2, c + 1, m), f(h1, h2 + 2, c + 1, m),
             f(h1 * 2, h2, c + 1, m), f(h1, h2 * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for h2 in range(16, 63):
    if f(9, h2, 0, 4):
        print(f'(9, {h2})')

