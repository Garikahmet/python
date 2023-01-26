# напишите программу, которая будет на вход принимать число N и выводить числа от -N до N.

number = int(input())
for i in range(-number, number):
    print(i, end=", ")
print(number)

# N = int(input())
# print(*range(-N, N + 1), sep=", ")