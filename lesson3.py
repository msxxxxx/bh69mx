# # age = 34
# # name = 'Alex'
# # is_human = True
# #
# # text1 = 'Hello' + name + 'age' + str(is_human)
# # text2 = 'Hello %s your age %d is human %d' %(name, age, is_human)
# # text3 = 'Hello {} age {} is human {}'.format(name, age, is_human)
# # text4 = f'Hello {name} age {age} is human {is_human}'
# # print(text1)
# # print(text2)
# # print(text3)
# # print(text4)
# # print(text4)
# # print('\N{fire}')
# # # 3 и 4 часто используются
#
# # print('hello'.center(16,'-'))
# # print('hello'.zfill(16))
#
# sent = input("input 3 word:")
# print(len(sent))
# sent_1 = sent.split()
# print(sent_1[2], sent_1[1], sent_1[0])
#
# f_space = sent.find(' ')
# l_space = sent.rfind(' ')
# print(f_space, l_space)

#palindrom
# text = input("input word:")
# text1 = text.lower()
# text2 = text1[::-1]
# print(text2)
# print(text1 == text2)

# text = input().lower()
# print(text == text[::-1])

# son = int(input())
# dad = int(input())
#
# print(dad-2*son)

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

z1 = x1 - y1
z2 = x2 - y2

l = (z1**2 + z2**2) ** 0.5
print(l)






