# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

number =  input("Введите дробное число: ")
comma_pos = number.find(",")
if "," not in number:
    print("NO")
else:
    print(number[comma_pos + 1])


# a = float(input())
# if a % 1 == 0:
#    print("NO")
#else:
#    print(int(a * 10) % 10)

a = input()
if "." in a:
    ind = a.index(",")
    print(a[ind + 1])
else:
    print("NO")