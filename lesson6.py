
#TODO написать функцию принимающую 3 целочисленных аргумента (a, b, c)
#и возвращасписок чисел геометрической поргрессии от a до b с множителем c
#a=2 b = 100 c =2

# def progress(a, b, c):
#     lst = []
#     while a < b:
#         lst.append(a)
#         a *= c
#     print(lst)
#
# progress(2, 100, 2)

#TODO написать функцию average, принимающую неопределенное кол-во
#чисел и возвращает среднее значение с точностью до 2
#
# def average(*args):
#     for i in args:
#         i += i
#         print(i/len(args))
# average(1,2,3,4,5,6,7,34,100)

#LEGB
# Local
# Enclosing
# Global
# BuiltIn
# map filter lambda zip почитать

#TODO Написать функцию, принимающую список чисел и возвращающая аккумулятивную сумму
# пример [1,2,3,4,5]
# ответ [1,3,6,10,15]

# def akum(*numbers):
#     s = 0
#     res = []
#     for number in numbers:
#         s += number
#         res.append(s)
#     print(res)
#
# akum(1,2,3,4,5)
#
# from string import ascii_lowercase
# text = 'gjgjgjgj'
# def is_pangram(text):
#     text = text.lower()
#     for letter in ascii_lowercase:
#         if letter not in text:
#             return False
#     return True
#
# is_pangram(text)

