for x in range(100):
    for y in range(100):
        for z in range(100):
            if x + 2 * y + 3 * z == 56 and \
               x + y + 3 * z == 44 and \
               y + z == 19:
                print(x + y + z + 2, x, y, z)
