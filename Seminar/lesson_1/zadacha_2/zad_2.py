# Напишите программу, которая на вход принимает 5 чисел и находит максимальное число

some_list = []
for _ in range(5):
    x = int(input())
    some_list.append(x)
maxx = some_list[0]
# print(max(some_list))
for el in some_list:
    if el > maxx:
        maxx = el
print(maxx)

# вариант №2

# maxx = int(input())
# for _ in range(4):
#     x = int(input())
#     if x > maxx:
#         maxx = x
# print(maxx)

