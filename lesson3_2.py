# Пользователь вводит 3 числа, найти среднее арифмитическое с
# точность 3
num1 = int(input("Input 1st number: "))
num2 = int(input("Input 2d number: "))
num3 = int(input("Input 3d number: "))
average = (num1 + num2 + num3)/3
print("average: ", round(average, 3))
