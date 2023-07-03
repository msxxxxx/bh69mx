# Дан список содержащий словари, в каждом словаре может быть или не быть ключ price.
# Значение ключа, при его наличии, является число (int, float).
# Необходимо рассчитать среднее значение price среди словарей у которых есть данный ключ.

lst = [
    {'fruit': 'banana', 'price': 5.3},
    {'fruit': 'limon'},
    {'fruit': 'orange', 'price': 6},
    {'fruit': 'red', 'price': 10},
    {'fruit': 'green', 'price': 3.3},
]
s = 0
c = 0
for i in lst:
    try:
        if i['price']:
            c += 1
    except KeyError:
        pass
    try:
        n = i['price']
        s += n
    except KeyError:
        pass

print('medium price: ', round(s/c, 2))


