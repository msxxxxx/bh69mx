# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами

name = input("Username: ")
age = int(input("Age: "))
city = input("City: ")
notification1 = "Hello %s %d live in %s" % (name, age, city)
notification2 = "Hello {} {} live in {}".format(name, age, city)
notification3 = f"Hello {name} {age} live in {city}"
print(notification1)
print(notification2)
print(notification3)