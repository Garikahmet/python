# Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

import random
n = int(input("Сколько элементов? "))
list1 = []
for i in range(n):
    list1.append(random.randint(1, 5))
print('Cделан такой список -', list1)


max_count = 0
for i in range(0, len(list1)):
    if list1.count(list1[i]) > max_count:
        max_count = list1.count(list1[i])
    print(max_count)
