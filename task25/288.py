# from re import fullmatch
#
# for i in range(10**7, 10**8):
#     if fullmatch(r'1\d58\d*129', str(i)):
#         if i % 117 == 0 and i % 119 != 0 and i % 121 != 0:
#             print(i, i // 117)
#         elif i % 117 != 0 and i % 119 == 0 and i % 121 != 0:
#             print(i, i // 119)
#         elif i % 117 != 0 and i % 119 != 0 and i % 121 == 0:
#             print(i, i // 121)

# 10581129 90437
# 12589129 105791
# 13582129 112249
# 17587129 147791

for x in '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
    for y in '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
        t = '1' + x + '58' + y + '129'
        i = int(t)
        if i % 117 == 0 and i % 119 != 0 and i % 121 != 0:
            print(i, i // 117)
        elif i % 117 != 0 and i % 119 == 0 and i % 121 != 0:
            print(i, i // 119)
        elif i % 117 != 0 and i % 119 != 0 and i % 121 == 0:
            print(i, i // 121)
