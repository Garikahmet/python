# Примеры использования filter, lambda, map, zip, enumerate, list comprehension

# def even(x):
#     return x % 2 == 1

# def a(x):
#     return x < 0

# some_list = [1, 5, 1, 2, 3]
# new_list = list(filter(lambda x: x < 0, some_list))
# for i in new_list:
#     print(i)

# some_list = ['hello', 'world', 'hi', 'banana', 'orange']
# new_list = filter(lambda word: 'h' not in word, some_list)
# print(list(new_list))

# some_list = [1, 2, 3, 4, 5]
# new_list = map(str, some_list)
# print(list(new_list))


# some_list = [1, 2, 3, 4, 5]
# new_list = list(map(lambda x: x ** 2, some_list))
# print(new_list)

# first_list = [1, 2, 3, 4, 5]
# second_list = list(map(str, first_list))
# print(list(zip(first_list, second_list)))

# some_dict = {}
# for i, j in zip(first_list, second_list):
#     some_dict[i] = j
# print(some_dict)

# some_list = ['banana', 'orange', 'grape']
# print(list(enumerate(some_list)))
# for i, j in enumerate(some_list):
#     print(i, j)


# some_list = [i ** 2 for i in range(1, 10) if i % 2 == 0]
# print(some_list)

import random

some_list = [random.randint(1, 10) for i in range(10)]
print(some_list)