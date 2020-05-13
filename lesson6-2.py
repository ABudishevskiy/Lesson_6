# Реализовать RLE сжатие для списка.
#
# [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1]
# [(2, 2), (3, 4), (2, 6), (1, 7), (4, 9), (2, 5), (1, 1)]

a = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1]
b = []
count = 1
for i in range(len(a) - 1):
    if a[i] == a[i+1]:
        count = count + 1
        chis = a[i]
        if i == (len(a) - 2):
            b.append((count, a[i]))
    else:
        b.append((count, a[i]))
        count = 1
if a[-2] != a[-1]:
    b.append((1, a[-1]))
print(b)