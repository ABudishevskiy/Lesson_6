# Найти самую длинную последовательность из одинаковых чисел в списке, вывести длину и само число.
#
#
#
# [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1, 9, 9]
# '9' - 4

a = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1, 9, 9]
count = 1
maxc =0
for i in range(len(a) - 1):
    if a[i] == a[i+1]:
        count = count + 1
        chis = a[i]
    else:
        if count > maxc:
            maxc = count
        count = 1
print('\'{}\' - {}'.format(chis, maxc))