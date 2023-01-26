# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# string = input('Введите исходную строку:')
# sinbol = input('Введите искомое слово')
# word_list = string.split(' ')
# count = 0
# number_word = 0
# for i in word_list:
#     if i == sinbol:
#         if  count == 2:
#             print(number_word)
#             exit()
#         else:
#             count += 1
#     number_word += 1

a = input().split()
find_str = input()
count = 0
for i in range(len(a)):
  if a[i] == find_str:
    count += 1
    if count == 2:
      print(i)
      break
else:
  print(-1)
