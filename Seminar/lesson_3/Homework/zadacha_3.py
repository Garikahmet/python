# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = list(map(float, input().split()))
new_list = [round(i % 1, 2) for i in list if i % 1 != 0]
print(max(new_list) - min(new_list))