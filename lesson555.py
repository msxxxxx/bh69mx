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

# d = {1: "a", 2: "b"}
# list(d.values())
for i in data:
    d = list(i.values())
    print(d)
    for n in d:
        print(n)

# if __name__ == '__main__':
#     data = [2, 3, 6, 12, 31, 34, 75]
#     number_to_find = 13
#     iterative_number_index = iterative_binary_search(0, len(numbers) - 1, numbers, number_to_find)
#
#     if iterative_number_index != -1:
#         print(f"Iterative Binary Search: Number {number_to_find} found in the list at index {iterative_number_index}")
#     else:
#         print(f"Iterative Binary Search: Number {number_to_find} not found in the list")
