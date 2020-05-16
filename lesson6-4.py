# Поиск минимума с переменным числом аргументов в списке.
#
# def min(*args): ....
def minx(*args):
    m = args[0]
    for i in args:
        if i < m:
            m = i

    return m
print(minx(1, 5, 7, 45, 0, -1, -18))