# Дан список словарей, каждый словарь имеет ключи: category_id, title, price.
# Значение ключа category_id является целое положительное число,
# значением ключа name - str, а значение ключа price - float.
# Те словари, у которых ключ category_id = 1, необходимо удалить,
# а те у которых category_id = 2, необходимо уменьшить price на 5%.
# Остальные словари оставляем без изменений.

lst = [
    {'category_id': 1, 'title': 'name1', 'price': 4.3},
    {'category_id': 2, 'title': 'name2', 'price': 1.5},
    {'category_id': 3, 'title': 'name3', 'price': 2.4},
    {'category_id': 1, 'title': 'name4', 'price': 5.6},
    {'category_id': 2, 'title': 'name5', 'price': 6.4}
]

for i in lst[0:]:
    if i['category_id'] == 1:
        del i
    elif i['category_id'] == 2:
        i['price'] = i['price'] * 0.95
        print(i)
    else:
        print(i)

