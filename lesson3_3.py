# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами

name = input("Username: ")
age = int(input("Age: "))
city = input("City: ")
notification1 = "Hello %s your age %d you live in %s" % (name, age, city)
notification2 = "Hello {} your age {} you live in {}".format(name, age, city)
notification3 = f"Hello {name} your age {age} you live in {city}"
print(notification1)
print(notification2)
print(notification3)
