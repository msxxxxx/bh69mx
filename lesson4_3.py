# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

users = {}
n = int(input('n = '))
for i in range(0, n):
    name = input('name: ')
    email = input('email: ')
    users[n] = {
        {name: email}
    }
    print(users)