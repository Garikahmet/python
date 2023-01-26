# Задайте последовательность чисел. Напишите программу, которая выведет список непвторяющихся элементов исходной последовательности.

from time import perf_counter
start = perf_counter

a = list(map(int, input().split()))
for el in a:
    if a.count(el) == 1:
        print(el, end = " ")

end = perf_counter
print(end - start)

# start = perf_counter()
# count1 = 1
# use_number = set()
# for ind in range(len(a)):
#     if a[ind] not in use_number:
#         use_number.add(a[ind])
#         for ind2 in ra