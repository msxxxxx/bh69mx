# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

# способ через цикл
# users = {}
# n = int(input('n: '))
# for i in range(0, n):
#     users[i] = {
#         input('name: '): input('email: ')
#     }
# print(users)

# способ через dict comprehension
n = int(input('n: '))
d = {i: {'name': input('name: '), 'email': input('email: ')} for i in range(n)}
print(d)
