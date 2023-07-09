# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

dict_users = {
    1: {'firstname': 'max', 'lastname': 'ivanov', 'phone': '123', 'email': 'm@i'},
    2: {'firstname': 'igor', 'lastname': 'smirnov', 'phone': '133', 'email': 'i@s'},
    3: {'firstname': 'lena', 'lastname': 'sidorova', 'phone': '222', 'email': ''},
    4: {'firstname': 'olga', 'lastname': 'petrova', 'phone': '222'},
    5: {'firstname': 'koly', 'lastname': 'cvetkov', 'phone': '222', 'email': 'k@cv'}
}

def users(dict_users):
    for id, info in dict_users.items():
        if not info.get('email'):
            print(info['firstname'] + ' ' + info['lastname'])


users(dict_users)
