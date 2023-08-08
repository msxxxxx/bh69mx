# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

def perevod(n):
    print('Decimal before: ', n)
    bin = ''
    while n > 0:
        bin = str(n % 2) + bin
        n = n // 2
    print('Binary: ', bin)
    c = 0
    for i in range(0, len(bin)):
        c = c+int(bin[i])*(2**(len(bin)-i-1))
    print('Decimal after: ', c)

perevod(202)
