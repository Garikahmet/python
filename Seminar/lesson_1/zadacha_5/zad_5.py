# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 0 или 15, но не 30.

n = int(input("Введите число: "))
if (n % 6 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
    print("Yes")
else:
    print("No")
    

