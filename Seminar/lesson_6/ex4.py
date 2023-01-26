# Создайте список из случайных чисел. Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2

import random
n = int(input("Сколько элементов? "))
list1 = []
for i in range(n):
    list1.append(random.randint(1, 10))
print('Cделан такой список -', list1)

max_num = max(list1)
new_list = []
for i in range(0, len(list1)):
    if list1[i] != max_num:
        new_list.append(list1[i])
max_num = max(new_list)
print(new_list,max_num)