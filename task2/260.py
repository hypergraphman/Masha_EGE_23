def trash(A1, A2, A3, A4):
    tab = []
    tab.append('{}{}{}{}{}{}'.format(A1, A2, A3, A4, '1', '2'))
    for a1 in 0, 1:
        for a2 in 0, 1:
            for a3 in 0, 1:
                for a4 in 0, 1:
                    f1 = int((a4 <= a3) == (a2 <= a1))
                    f2 = int((a4 <= a3) and (a1 != a2))
                    tab.append('{}{}{}{}{}{}'.format(a1, a2, a3, a4, f1, f2))
    return tab


from itertools import permutations
from fnmatch import fnmatch


for x, y, z, w in permutations('xyzw'):
    t = trash(x, y, z, w)
    k = 0
    for name in '?0000?', '?011?0', '00?001':
        for line in t:
            if fnmatch(line, name):
                k += 1
                break
    if k == 3:
        print(t[0])
