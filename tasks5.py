#Вводится число, необходимо подсчитать его факториал

n = int(input('n = '))
s = 1
if n == 0:
    print('n! = 1')
elif n > 0:
    nlist = [i for i in range(1, n+1)]
    for x in nlist:
        s *= x
    print(s)
else:
    print('Negative')


