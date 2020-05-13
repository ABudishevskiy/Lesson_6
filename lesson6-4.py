# Поиск минимума с переменным числом аргументов в списке.
#
# def min(*args): ....
def minx(*args):
    return min(*args)
print(minx(1, 5, 7, 45, 0, -1))