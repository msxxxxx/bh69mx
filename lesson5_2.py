# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

num1 = int(input('num1 = '))
num2 = int(input('num2 = '))
operation = input('input operation: + - / * ')

if operation == '+':
    print(num1 + num2)
if operation == '-':
    print(num1 - num2)
if operation == '/':
    print(num1 / num2)
if operation == '*':
    print(num1 * num2)