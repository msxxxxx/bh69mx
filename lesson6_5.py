# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

lst = [1, 2, 3, 4, 5, 6, 7, 8]
def rvrs(lst):
    for i in range(len(lst)):
        last_i = lst.pop()
        lst.insert(i, last_i)
    print(lst)


rvrs(lst)
