#Напишите программу, которая принимает на вход числа и проверяет, является ли число квадратом другого.

number1 = int(input())
number2 = int(input())
if number1 ** 2 == number2 or number2 ** 2 == number2:
    print("да")
else:
    print("нет")
