# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

lst = [44, 1, 2, 3, 1, 4, 8, 5, 6, 7, 8, 9, 10]
ch = []
n_ch = []
def sort_numb(lst):
    for i in lst:
        if not i % 2:
            ch.append(i)
            ch.sort()
        else:
            n_ch.append(i)
            n_ch.sort()
    lst = ch + n_ch
    print(lst)

sort_numb(lst)
