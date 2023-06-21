# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

# num1 = (input("Input 1 numbers: "))
# num2 = (input("Input 2d numbers: "))
# num3 = (input("Input 3d numbers: "))
# # input_string = input("Enter 3 elements separated by comma: ")
str1 = input("input:")
list2 = str1.split(" ")
print(type(list2))
count_pos = 0
count_neg = 0
for num in list2:
    if num > 0:
        count_pos = count_pos + 1
    if num < 0:
        count_neg = count_neg + 1
print("Positive", count_pos)
print("Negative", count_neg)
