# # n = int(input('deposit: '))
# # proc = int(input('procent: '))
# # proc = proc/100
# # year = 0
# # while n < 2*n:
# #     year += 1
# #     n *= proc
# # print(year)
#
# amount = int(input('sum: '))
# coins = [25, 10, 5, 1]
# count = 0
# for coin in coins:
#     count += amount // coin
#     amount -= (amount // coin) * coin
# print(count)
# #
# #
#

# list = [i for i in [1, 2, 3, 4, 5, 6, 7, 8, 22] if not i % 2]
# print(list)
# numbers = [1, 2, 3, 3, 4, 5, 22, 6, 7, 8, 22]
# for i in range(len(numbers) -1, -1, -1):
#     if numbers[i] % 2:
#         del numbers[i]
# print(numbers)

#n = str(input('number'))
# max_count = 0
# for i in n:
#     if int(i) > max_count:
#         max_count = int(i)
# print(max_count)

data = [
    {'name': 'Name1', 'age': 12},
    {'name': 'Name2', 'age': 13},
    {'name': 'Name3', 'age': 15},
    {'name': 'Name4', 'age': 18},
    {'name': 'Name5', 'age': 22},
    {'name': 'Name6', 'age': 34},
    {'name': 'Name7', 'age': 37}
]
lst = []
# for i in data:
#     lst = ''.join(str(i['age']))
#     print(lst)

for n in data:
    j = int(n['age'])
#    print(j)
    lst.append(j)
print(lst)







elem = 37

low = 0
high = len(lst) - 1

while low <= high:
    middle = (low + high) // 2
    if lst[middle] == elem:
        print(middle)
        break
    elif lst[middle] > elem:
        high = middle - 1
    else:
        low = middle + 1
