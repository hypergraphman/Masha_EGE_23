from re import fullmatch
from fnmatch import fnmatch

for i in range(50068, 10 ** 10, 50068):
    # if fullmatch(r'9\d979\d*8', str(i)):
    if fnmatch(str(i), '9?979*8'):
        if '0' in str(i):
            print(i, i // 50068)
