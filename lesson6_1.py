# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
# 20 - > 0101
# 0101 - > 20

# n = input('n = ')
def perevod(n):
    print('Decimal before: ', n)
    r = bin(n)
    l = str(r[2:])
    print('Binary: ', l)
    c = 0
    for i in range(0, len(l)):
        c = c+int(l[i])*(2**(len(l)-i-1))
    print('Decimal after: ', c)

perevod(22)
