# Дан список из чисел. Нужно реализовать подсчет суммы чисел на отрезке списка.
# На вход даются запросы в виде пары чисел - индекс начала и конца интервала
# для суммирования - нужно выводить сумму элементов списка для каждого запроса.
#
# * Как это реализовать если список длиной больше 1 млн и запросов больше 1 млн ?

import random
lis = []
for i in range(110):
    lis.append(random.randint(1, 1000))
print(lis)
a = int(input('begin'))
b = int(input('end'))
def sumsl(a, b, lis):
    count = 0
    for i in range(a, b+1):
        count = count + lis[i]
    return count

print(sumsl(a, b, lis))