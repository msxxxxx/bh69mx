# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно

lst = [1, 2, 3, 'sd', 4, 'asas', 'ererer', (1, 2, 3)]
lst = list(filter(lambda i: isinstance(i, str), lst))
print(lst)
