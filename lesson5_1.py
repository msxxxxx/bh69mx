# Вывести первые N чисел кратные M и больше K

n = 5
m = 3
k = 10
s = [i for i in range(k, k+m, m) if not i % m]
print(s)


