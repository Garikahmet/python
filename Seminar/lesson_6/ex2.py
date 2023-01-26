# Создайте список из случайных чисел. Найдите номер его последнего локального максимума (локальный максимум — это элемент, который больше любого из своих соседей).

import random
n = int(input("Сколько элементов? "))
list1 = []
for i in range(n):
    list1.append(random.randint(1, 10))
print('Cделан такой список -', list1)

for i in range(1, len(list1) - 1):
    if list1[i-1] < list1[i] > list[i+1]:
        temp = i
print(temp)
