# # Пользователь вводит 3 числа, сказать сколько из них положительных
# # и сколько отрицательных
#
a = int(input("Input num a: "))
b = int(input("Input num b: "))
c = int(input("Input num c: "))
a1 = abs(a)
b1 = abs(b)
c1 = abs(c)
x = str(a == a1)
y = str(b == b1)
z = str(c == c1)
text = x + z + y
print("Positive: ", text.count("True"))
print("Negative: ", text.count("False"))
# count = 0
# neg = 0
# a = int(input("Input 1st num: "))
# if a > 0:
#     count += 1
# else:
#     neg += 1
# b = int(input("Input 2d num: "))
# if b > 0:
#     count += 1
# else:
#     neg += 1
# c = int(input("Input 3d num: "))
# if c > 0:
#     count += 1
# else:
#     neg += 1
# print("positive: ", count, "Negative: ", neg)
#

