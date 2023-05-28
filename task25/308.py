from itertools import product

*nums, = product('0123456789', repeat=6)
for num in nums:
    num = ''.join(num)
    if int(num) > 0 and int(num) % (sum(map(int, num)) ** 3) == 0:
        num = '1234' + num
        if int(num) % 137 == 0:
            print(num, int(num) // 137)