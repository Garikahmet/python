# Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random

some_list = [random.randint(1, 10) for i in range(10)]
print(some_list)

count = 0 
new_list = []
for i in some_list:
    if i not in new_list:
        count += 1
        new_list.append(i)
print(len(new_list))