# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



a = list(map(int, input().split()))
sum = 0
for i in range(len(a)):
    if i % 2 != 0:
        sum += a[i]
print({sum})
