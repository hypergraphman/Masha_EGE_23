from itertools import product

# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
for x, y, z, w in product((0, 1), repeat=4):
    if not ((w <= z) and (x or y)) <= ((y == w) or (z and (not x))):
        print(x, y, z, w)
