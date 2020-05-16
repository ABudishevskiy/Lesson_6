# Дан список большой вложенности, нужно его развернуть в 1d
#
# [[], [1, 2], [2, 3, [1, 2]], [1, 2, 3]]

lis = [[], [1, 2], [2, 3, [1, [9, 6], 2, [7, 8, [4, 5]]]], [1, 2, 3]]
# def rev(a):
#     newlist = []
#     for i in a:
#         if isinstance(i, list):
#             count = 0
#             for k in i:
#                 if isinstance(k, list):
#                     for l in rev(i)[count: ]:
#                         newlist.append(l)
#                 else:
#                     count = count + 1
#                     newlist.append(k)
#         else:
#             newlist.append(i)
#     return newlist
def rev2(a):
    newlist = []
    for i in a:
        if isinstance(i, list):
            newlist.extend(rev2(i))
        else:
            newlist.append(i)
    return newlist

print(rev2(lis))