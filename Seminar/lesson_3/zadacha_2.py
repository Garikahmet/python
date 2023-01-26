# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# string = input('Введите исходную строку:')
# sinbol = input()
# sin_list = ''
# word_list = string.split(' ')
# for i in word_list:
#     for j in i:
#         if j == sinbol:
#             print('Yes')
#             exit()

# print('no')

a = input.split()
number = input()
for i in a:
    if number in i:
        print('yes')
    break
else:
  print('no')
