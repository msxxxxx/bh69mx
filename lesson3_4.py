# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

count = 0
neg = 0
a = int(input("Input 1st num: "))
if a > 0:
    count += 1
else:
    neg += 1
b = int(input("Input 2d num: "))
if b > 0:
    count += 1
else:
    neg += 1
c = int(input("Input 3d num: "))
if c > 0:
    count += 1
else:
    neg += 1
print("positive: ", count, "Negative: ", neg)

