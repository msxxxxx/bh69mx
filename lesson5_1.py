# Вывести первые N чисел кратные M и больше K
# 12,15,18,21,24

c = 0
n = int(input('n = '))
m = int(input('m = '))
k = int(input('k = '))
lst = []
while c < k:
    c += 1
    while c >= k:
        c += 1
        if c % m == 0:
            lst.append(c)
            if len(lst) == n:
                break
print(lst)
