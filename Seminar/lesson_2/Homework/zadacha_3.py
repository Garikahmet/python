# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} 
# Сумма 9.06

N = int(input())
out_dict = {}
for i in range(1, N + 1):
    out_dict[i] = round((1 + 1/i) ** i, 2)
print(out_dict)
print(f'\n Сумма: {sum(out_dict)}')