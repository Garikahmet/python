# Напишите программу, которая принимает на вход чило N и выдает поледовательность из N членов

n = int(input())
print('Для n =', n, end = ': ')
for i in range(n - 1):
    print((-3)**i,end=', ')
print((-3) ** (n - 1 ))

# n = int(input())
# out_list = []
# for i in range(n):
#   out_list.append((-3) ** i,)
# print(*out_list, sep=', ')