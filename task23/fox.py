def f(s, e):
    if s < e:
        return 0
    if s == e:
        return 1
    return f(s - 3, e) + f(s // 2, e)


print(f(73, 13) * f(13, 2))