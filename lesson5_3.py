# **Вывести четные числа от 2 до N по 5 в строку

n = int(input('n = '))
new_list = [x for x in range(2, n+1) if not x % 2]
m = 5
for i in range(0, len(new_list), m):
    nlist = new_list[i:i + m]
    s = ' '.join(str(x) for x in nlist)
    print(s)

