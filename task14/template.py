def n_to_p(n, p):
    res = ''
    while n > 0:
        res = '0123456789ABCDEF'[n % p] + res
        n //= p
    return res


print(n_to_p(2**2014 - 4**650 - 38, 2).count('1'))