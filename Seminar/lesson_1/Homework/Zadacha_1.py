# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

n = int(input("Введите число: "))
if 6 <= n <= 7:
    print("Yes")
elif 1 <= n <= 5:
    print("No")