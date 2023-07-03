#Вводится число N, необходимо вывести N чисел Фибоначчи

n = int(input('n = '))
lst = []
fnum1 = fnum2 = 1
for i in range(0, n):
    fnum1, fnum2 = fnum2, fnum1 + fnum2
    lst.append((fnum2))
print(lst)
