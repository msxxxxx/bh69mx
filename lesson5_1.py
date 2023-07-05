# Вывести первые N чисел кратные M и больше K

n = int(input('n = '))
m = int(input('m = '))
k = int(input('k = '))
lst = []

while len(lst) < n:
    k += 1
    if k % m == 0:
        lst.append(k)
print(lst)


