# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];

a = list(map(int, input().split()))
l = len(a) // 2 + 1 if len(a) % 2 != 0 else len(a) // 2
new_a = [a[i] * a[len(a) - i - 1] for i in range(l)]
print(new_a)