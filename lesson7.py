# def m_ran(s, st, step):
#     for i in range(s, st, step):
#         yield i ** 2

# написать генератор геометрической прогрессии с множителем multiplier

# def m_ran(s, st, multiplier):
#     while s < st:
#         yield s
#         s *= multiplier
#
# for i in m_ran(2, 19, 3):
#     print(i)

# counter_words = {'vowels': 0, 'consonants': 0}
# text = 'aaadfhjdfhkd3'
#
#
# def count_words(text):
#     text = text.lower()
#     vowels = 'aeiou'
#     for i in text:
#         if i .isalpha():
#             if i in vowels:
#                 counter_words['vowels'] += 1
#             else:
#                 counter_words['consonants'] += 1
#     return counter_words
#
#
# print(count_words(text))

# def validate_year(year):
#     return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
#
#
# print(validate_year(2000))
# print(validate_year(2100))
# print(validate_year(2104))

#степень в рекурсии
def stepen_recursive(base, exp):
    if exp > 1:
        base *= stepen_recursive(base, exp-1)
    return base

print(stepen_recursive(5, 3))